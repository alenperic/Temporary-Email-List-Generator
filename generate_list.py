from datetime import datetime
import os
import shutil
import argparse
import pandas as pd
import urllib.request
import urllib.error

# Function to rename existing new_list.csv to old_list.csv and backup old_list.csv
def rename_existing_new_list():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m%Y")
    if os.path.exists("new_list.csv"):
        if os.path.exists("old_list.csv"):
            backup_old_list_name = f"old_list_{formatted_date}.csv"
            shutil.copy("old_list.csv", backup_old_list_name)
            print(f"Copied old_list.csv to {backup_old_list_name}.")
        shutil.move("new_list.csv", "old_list.csv")
        print("Renamed existing new_list.csv to old_list.csv.")
    else:
        print("No existing new_list.csv found.")

# Function to check for required files
def check_required_files():
    if not (os.path.exists("old_list.csv") or os.path.exists("sources.txt") or os.path.exists("github_file.txt")):
        print("Error: Missing all required files - old_list.csv, sources.txt, and GitHub URLs.")
        return False
    return True

# Import the main CSV file
def import_csv(file_path):
    df = pd.read_csv(file_path, header=None)
    return df

# De-duplicate the entries
def deduplicate(df, column):
    return df.drop_duplicates(subset=[column])

# Remove entries that are in the whitelist and print them
def remove_whitelisted(df, whitelist_path, column):
    whitelist_df = pd.read_csv(whitelist_path, header=None)
    removed_entries = df[df[column].isin(whitelist_df[column])]
    removed_entries.to_csv('allowlist_removed.txt', index=False, header=False)
    df = df[~df[column].isin(whitelist_df[column])]
    return df

# Save as a CSV file
def save_csv(df, file_path):
    df.to_csv(file_path, index=False, header=False)

# Compare to a past list and count new entries
def compare_and_count_new_entries(df, past_df, column):
    new_entries = df[~df[column].isin(past_df[column])]
    return new_entries, len(new_entries)

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description='Process CSV files.')
    parser.add_argument('-L', '--local-file', help='Specify a local file to use', required=False, default="old_list.csv")
    parser.add_argument('-C', '--column', help='Specify the column to use', required=False, default=0, type=int)
    parser.add_argument('-D', '--github-file', help='Specify a local .txt file containing GitHub repos', required=False)
    parser.add_argument('-S', '--sources-file', help='Specify a local .txt file containing data source URLs', required=False, default="sources.txt")
    parser.add_argument('-M', '--main-file', help='Specify the main CSV file', required=False, default="new_list_unedited.csv")
    parser.add_argument('-W', '--whitelist-file', help='Specify the whitelist CSV file', required=False, default="allowlist.csv")
    args = parser.parse_args()

    # Check for required files and exit if all conditions are met
    if not check_required_files():
        print("Exiting due to missing required files.")
        exit(1)
    
    # Rename existing new_list.csv if exists
    rename_existing_new_list()

    # Fallback logic for main data frame
    if os.path.exists(args.main_file):
        main_df = import_csv(args.main_file)
    elif os.path.exists(args.local_file):
        print(f"{args.main_file} not found. Using {args.local_file} as the data source.")
        main_df = import_csv(args.local_file)
    else:
        print("Error: Neither new_list_unedited.csv nor old_list.csv found.")
        exit(1)

    # Rest of your existing code for CSV processing, deduplication, etc.
    main_df = deduplicate(main_df, args.column)
    main_df = remove_whitelisted(main_df, args.whitelist_file, args.column)
    save_csv(main_df, 'new_list.csv')

    past_df = import_csv(args.local_file)
    new_entries, count_new_entries = compare_and_count_new_entries(main_df, past_df, args.column)
    print(f"Number of new entries: {count_new_entries}")
    save_csv(new_entries, 'new_entries.csv')

    # Compare to a past list and count new entries
    new_entries, count_new_entries = compare_and_count_new_entries(main_df, past_df, args.column)
    print(f"Number of new entries: {count_new_entries}")
    save_csv(new_entries, 'new_entries.csv')

    # Generate Output.txt with summary statistics
    with open('Output.txt', 'w') as f:
        f.write(f"Old list entries: {len(past_df)}\n")
        f.write(f"New entries: {count_new_entries}\n")
        f.write(f"New list: {len(main_df)}\n")
        addition_total = len(past_df) + count_new_entries
        f.write(f"Addition total: {addition_total}\n")
        discrepancy = addition_total - len(main_df)
        f.write(f"Discrepancy: {discrepancy}\n")
