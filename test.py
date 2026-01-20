import pandas as pd

file_path = '/Users/goels2/Downloads/ADSK Daily and Monthly ICC (1).xlsx'

# Get all sheet names
sheet_names = pd.ExcelFile(file_path).sheet_names

# Get the last 7 sheet names
last_7_sheets = sheet_names[-12:-5]

# print("Last 7 sheets:", last_7_sheets)

dfs = []
for sheet in last_7_sheets:
    # Parse date from sheet name, e.g., '1-7' -> '01-07'
    try:
        month, day = map(int, sheet.split('-'))
        date_str = f"{month:02d}-{day:02d}"
    except Exception:
        # If sheet name is not in expected format, skip
        continue

    df = pd.read_excel(file_path, sheet_name=sheet)
    df.insert(0, 'Date', date_str)
    dfs.append(df)

# Merge all DataFrames
merged_df = pd.concat(dfs, ignore_index=True)

# Save merged DataFrame to Excel in the same location
# output_path = '/Users/goels2/Downloads/merged_last_7_tabs.xlsx'
# merged_df.to_excel(output_path, index=False)

# print(f"Merged data saved to {output_path}")

# print(merged_df.tail())

# Pivot: filter product_vertical, group by object_name, sum ICCs used
filtered_df = merged_df[merged_df['product_vertical'].isin(['Audience', 'Journey'])]

pivot_df = filtered_df.pivot_table(
    index='object_name',
    values='iccs_used',
    aggfunc='sum'
)
# Sort by 'iccs_used' column from largest to smallest
pivot_df = pivot_df.sort_values(by='iccs_used', ascending=False)

print(pivot_df.head(15))
