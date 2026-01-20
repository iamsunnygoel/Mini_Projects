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

# Group by object_name and Date, sum ICCs used per feature per date
grouped = filtered_df.groupby(['object_name', 'Date'], as_index=False)['iccs_used'].sum()

# Now, calculate the average ICCs used per feature across all dates
avg_iccs_per_feature = grouped.groupby('object_name')['iccs_used'].mean().sort_values(ascending=False)

print(avg_iccs_per_feature.head(21))

# Convert to DataFrame for better HTML formatting
avg_iccs_df = avg_iccs_per_feature.reset_index()
avg_iccs_df.columns = ['Feature', 'Average_ICCs_Used']

# Generate HTML table
html_table = avg_iccs_df.to_html(index=False, border=1, classes='dataframe', justify='center')

# Create a simple HTML page
html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Average ICCs Used per Feature</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h2 {{ text-align: center; }}
        table.dataframe {{
            margin-left: auto;
            margin-right: auto;
            border-collapse: collapse;
            width: 60%;
        }}
        table.dataframe th, table.dataframe td {{
            border: 1px solid #888;
            padding: 8px 12px;
            text-align: center;
        }}
        table.dataframe th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h2>Average ICCs Used per Feature</h2>
    {html_table}
</body>
</html>
"""

# Save the HTML page
output_html_path = '/Users/goels2/Downloads/avg_iccs_per_feature.html'
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_page)

print(f"HTML table saved to {output_html_path}")
