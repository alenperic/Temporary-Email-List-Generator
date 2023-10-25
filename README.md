# Temporary Email Domains List Creation Automation

## Description

This Python script is designed to automate the analysis and cleaning of temporary email domains from CSV files and serves to generate a blocklist for domains used to host temporary email domains. It performs the following tasks:

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
```
## Available Options

Here are the command-line options you can use when running the script:

- `-L, --local-file`: Specify a local file to use as the past dataset (Default: `old_list.csv`).
- `-C, --column`: Specify the column index to use for de-duplication and comparison (Default: `0`).
- `-D, --github-file`: Specify a local `.txt` file containing GitHub repository URLs. The script will fetch and append data from these repositories (Default: `sources.txt`).
- `-M, --main-file`: Specify the main CSV file to process (Default: `new_list_unedited.csv`).
- `-W, --whitelist-file`: Specify the whitelist CSV file to use for removing entries (Default: `allowlist.csv`).
