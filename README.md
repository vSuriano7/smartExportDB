# SQL Schema and Data Export Script

## Overview

This Python script generates a complete SQL file for a given database schema. It includes the Data Definition Language (DDL) to create all tables and constraints (including primary and foreign keys), as well as the Data Manipulation Language (DML) statements to insert data into the tables. The script ensures that all foreign key constraints are respected by creating tables and inserting data in the correct order.

## Features

- **Automatic Dependency Handling**: The script automatically detects dependencies between tables and sorts them to ensure that all referenced tables are created before the tables that reference them.
  
- **Comprehensive Export**: Generates both `CREATE TABLE` statements with primary and foreign key constraints and `INSERT` statements for all data in the tables.

- **Error Prevention**: Prevents foreign key constraint violations by ensuring that all tables and data are inserted in the correct order.

- **Cyclic Dependency Detection**: The script detects and raises an error if cyclic dependencies are found within the schema, helping to identify issues before executing the SQL file.

## Advantages

1. **Dependency-Aware Table Creation**: Unlike other tools, this script considers the dependencies between tables, ensuring the correct order of creation and avoiding foreign key errors.

2. **Data Insertion Order**: Data is inserted in the correct order, respecting foreign key relationships. This eliminates the risk of constraint violations during the import process.

3. **Customizable and Extensible**: Built with Python and SQLAlchemy, the script is easy to customize for different databases or specific project needs.

4. **Comprehensive Output**: The script generates a complete SQL file that can be used to recreate both the schema and the data in another database instance without manual adjustments.

5. **User-Friendly**: Simple to use and does not require extensive configuration or setup. Just provide the database URL and schema name, and the script handles the rest.

## Usage

1. Set up the necessary Python environment and install dependencies:
   ```bash
   pip install sqlalchemy pandas psycopg2-binary
   ```

2. Modify the script to set the correct `schema_name`, `db_url`, and `output_file` paths.

3. Run the script:
   ```bash
   python export_sql_schema.py
   ```

4. The generated SQL file will be saved at the location specified by `output_file`.

---

# Script per Esportazione di Schema e Dati SQL

## Panoramica

Questo script Python genera un file SQL completo per uno schema di database specificato. Include il linguaggio di definizione dei dati (DDL) per creare tutte le tabelle e i vincoli (inclusi chiavi primarie e chiavi esterne), nonché le istruzioni di manipolazione dei dati (DML) per inserire i dati nelle tabelle. Lo script garantisce che tutti i vincoli di chiave esterna siano rispettati creando le tabelle e inserendo i dati nell'ordine corretto.

## Caratteristiche

- **Gestione Automatica delle Dipendenze**: Lo script rileva automaticamente le dipendenze tra le tabelle e le ordina per garantire che tutte le tabelle referenziate siano create prima delle tabelle che le referenziano.
  
- **Esportazione Completa**: Genera sia le istruzioni `CREATE TABLE` con vincoli di chiave primaria e esterna, sia le istruzioni `INSERT` per tutti i dati nelle tabelle.

- **Prevenzione degli Errori**: Evita violazioni dei vincoli di chiave esterna garantendo che tutte le tabelle e i dati siano inseriti nell'ordine corretto.

- **Rilevamento di Dipendenze Cicliche**: Lo script rileva e genera un errore in caso di dipendenze cicliche all'interno dello schema, aiutando a identificare i problemi prima di eseguire il file SQL.

## Vantaggi

1. **Creazione di Tabelle Consapevole delle Dipendenze**: A differenza di altri strumenti, questo script considera le dipendenze tra le tabelle, garantendo l'ordine corretto di creazione ed evitando errori di chiave esterna.

2. **Ordine di Inserimento Dati**: I dati vengono inseriti nell'ordine corretto, rispettando le relazioni di chiave esterna. Questo elimina il rischio di violazioni dei vincoli durante il processo di importazione.

3. **Personalizzabile ed Estensibile**: Costruito con Python e SQLAlchemy, lo script è facile da personalizzare per diversi database o esigenze specifiche del progetto.

4. **Output Completo**: Lo script genera un file SQL completo che può essere utilizzato per ricreare sia lo schema che i dati in un'altra istanza di database senza necessità di aggiustamenti manuali.

5. **Facile da Usare**: Semplice da usare e non richiede configurazioni o setup estesi. Basta fornire l'URL del database e il nome dello schema, e lo script si occupa del resto.

## Utilizzo

1. Configura l'ambiente Python necessario e installa le dipendenze:
   ```bash
   pip install sqlalchemy pandas psycopg2-binary
   ```

2. Modifica lo script per impostare i percorsi corretti di `schema_name`, `db_url` e `output_file`.

3. Esegui lo script:
   ```bash
   python export_sql_schema.py
   ```

4. Il file SQL generato sarà salvato nella posizione specificata da `output_file`.
