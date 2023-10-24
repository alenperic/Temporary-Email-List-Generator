# Temporary Email Domains Processor

## Description

This Python script is designed to automate the analysis and cleaning of temporary email domains from CSV files. It performs the following tasks:

1. Imports a main CSV file.
2. De-duplicates entries based on a specified column.
3. Removes entries that match a given whitelist.
4. Saves the cleaned data as a new CSV file.
5. Compares the cleaned data to a past dataset to identify new temporary email domains.

The script also supports the option to fetch and append data from GitHub repositories.

## Dependencies

- Python 3.x
- Pandas library (`pip install pandas`)

## Usage

To run the script, navigate to the directory where the script is located and execute the following command:

```bash
python your_script_name.py [OPTIONS]
