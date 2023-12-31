# Temporary Email Domains List Creation Automation
This script may be used to automatically generate a list of temporary email domains in .csv format, which may then be used to block users signing up with temporary emails (such as 30 minute email services). The domain list sources are available across GitHub and need to be added to the *sources.txt* file.

## Description

This Python script is designed to automate the analysis and cleaning of temporary email domains from CSV files and serves to generate a blocklist for domains used to host temporary email domains. It performs the following tasks:

1. Imports a main CSV file.
2. De-duplicates entries based on a specified column.
3. Removes entries that match a given whitelist.
4. Saves the cleaned data as a new CSV file.
5. Compares the cleaned data to a past dataset to identify new temporary email domains.

The script also supports the option to fetch and append data from GitHub repositories.

## Output

The script generates several files:

- `new_list.csv`: The updated list of email domains.
- `new_entries.csv`: New entries that were not in the old list.
- `Output.txt`: Summary statistics, including the number of entries in the old list, the number of new entries, and any discrepancies.
- `allowlist_removed.txt`: A list of entries that were removed based on the allowlist.

## Dependencies

- Python 3.x
- Pandas library (`pip install pandas`)

## Usage

To run the script, navigate to the directory where the script is located and execute the following command:

```bash
python generate_list.py [OPTIONS]
```

## Available Options

Here are the command-line options you can use when running the script:

- `-L, --local-file`: Specify a local file to use as the past dataset (Default: `old_list.csv`).
- `-C, --column`: Specify the column index to use for de-duplication and comparison (Default: `0`).
- `-D, --github-file`: Specify a local `.txt` file containing GitHub repository URLs. The script will fetch and append data from these repositories (Default: `sources.txt`).
- `-M, --main-file`: Specify the main CSV file to process (Default: `new_list_unedited.csv`).
- `-W, --whitelist-file`: Specify the whitelist CSV file to use for removing entries (Default: `allowlist.csv`).

## Updates
Script now includes:
- Command-line arguments for various options
- Downloading data from specified URLs or from a text file
- Checking the accessibility of each URL based on HTTP status codes
- Printing the entries removed based on the whitelist

## Backup and Versioning

The script can be placed on a server and automatically executed with cronjob, or similar. In that case the script uses the previously generated new list in place of old list, backs up the old list and versions it with the current month and year for record-keeping.

## License

This project is licensed under the MIT License.
