import sqlalchemy
from sqlalchemy import create_engine, inspect
import pandas as pd
from collections import defaultdict, deque

def generate_sql_from_db(schema_name, db_url, output_file):
    # Create a database engine
    engine = create_engine(db_url)
    inspector = inspect(engine)
    
    # Gather metadata
    tables = inspector.get_table_names(schema=schema_name)
    table_dependencies = defaultdict(set)
    reverse_dependencies = defaultdict(set)

    # Determine dependencies between tables
    for table_name in tables:
        foreign_keys = inspector.get_foreign_keys(table_name, schema=schema_name)
        for fk in foreign_keys:
            referred_table = fk['referred_table']
            if referred_table:
                table_dependencies[table_name].add(referred_table)
                reverse_dependencies[referred_table].add(table_name)

    # Topological sort to ensure proper table creation order
    def topological_sort(dependencies):
        sorted_list = []
        no_deps = [table for table in tables if table not in dependencies]
        
        while no_deps:
            table = no_deps.pop()
            sorted_list.append(table)
            
            for dependent in reverse_dependencies[table]:
                dependencies[dependent].remove(table)
                if not dependencies[dependent]:  # No more dependencies left
                    no_deps.append(dependent)
                    del dependencies[dependent]
        
        if dependencies:
            raise Exception("Cyclic dependency detected in the schema, unable to sort tables.")
        
        return sorted_list

    creation_order = topological_sort(table_dependencies)
    
    with open(output_file, 'w') as file:
        # Write DDL statements
        for table_name in creation_order:
            columns = inspector.get_columns(table_name, schema=schema_name)
            primary_keys = inspector.get_pk_constraint(table_name, schema=schema_name)
            foreign_keys = inspector.get_foreign_keys(table_name, schema=schema_name)

            # Create table
            file.write(f"CREATE TABLE {schema_name}.{table_name} (\n")
            col_defs = []
            for column in columns:
                col_def = f"    {column['name']} {column['type']}"
                if column['nullable']:
                    col_def += " NULL"
                else:
                    col_def += " NOT NULL"
                col_defs.append(col_def)
            if primary_keys:
                pk_cols = ', '.join(primary_keys['constrained_columns'])
                col_defs.append(f"    PRIMARY KEY ({pk_cols})")
            file.write(",\n".join(col_defs) + "\n);\n\n")
            
            # Foreign key constraints
            for fk in foreign_keys:
                constraints = (f"FOREIGN KEY ({fk['constrained_columns'][0]}) REFERENCES {fk['referred_schema']}.{fk['referred_table']}"
                               f"({fk['referred_columns'][0]})")
                file.write(f"ALTER TABLE {schema_name}.{table_name} ADD CONSTRAINT {fk['name']} {constraints};\n")
            file.write("\n")

        # Write INSERT statements
        for table_name in creation_order:
            df = pd.read_sql_table(table_name, con=engine, schema=schema_name)
            if df.empty:
                continue
            file.write(f"INSERT INTO {schema_name}.{table_name} ({', '.join(df.columns)}) VALUES\n")
            insert_values = []
            for _, row in df.iterrows():
                values = ", ".join("'{}'".format(str(value).replace("'", "''")) if pd.notna(value) else 'NULL' for value in row)
                insert_values.append(f"({values})")
            file.write(",\n".join(insert_values) + ";\n\n")
    
    print(f"SQL file '{output_file}' generated successfully.")

# Usage
schema_name = 'pln'
db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'  # Adjust for your database
output_file = 'database_dump.sql'

generate_sql_from_db(schema_name, db_url, output_file)
