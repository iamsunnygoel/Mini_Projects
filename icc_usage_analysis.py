
import pandas as pd

# Load Excel
file_path = "/Users/goels2/Downloads/ADSK ICC Breakdown past 6 weeks (1).xlsx"
xls = pd.ExcelFile(file_path)

# Only process tabs with valid date ranges like '6-29 to 7-5'
skip_tabs = {"sheet2", "pattern", "insights"}  # lowercase for comparison
date_tabs = [sheet for sheet in xls.sheet_names if sheet.lower() not in skip_tabs]

# Helper to convert "6-29 to 7-5" to midpoint date
def get_midpoint_date(tab_name):
    year = 2025  # Update as needed
    try:
        start_str, end_str = tab_name.split(' to ')
        start = pd.to_datetime(f"{year}-{start_str.strip()}")
        end = pd.to_datetime(f"{year}-{end_str.strip()}")
        if end < start:
            end = end.replace(year=year + 1)  # Handle year rollover
        return start + (end - start) / 2
    except Exception as e:
        print(f"⚠️ Error parsing date from tab '{tab_name}': {e}")
        return pd.NaT

# Load data from each tab
all_data = []
for tab in date_tabs:
    df = pd.read_excel(file_path, sheet_name=tab)
    df['Date Range'] = tab
    df['Date Mid'] = get_midpoint_date(tab)
    all_data.append(df)

# Combine into one DataFrame
df_all = pd.concat(all_data, ignore_index=True)


# Analysis 1: Weekly trend
usage_trend = df_all.groupby('Date Mid')['iccs_used'].sum().reset_index()

# Analysis 2: By product_vertical
top_verticals = df_all.groupby(['Date Range', 'product_vertical'])['iccs_used'].sum().reset_index()

# Analysis 3: By product_feature
top_features = df_all.groupby(['Date Range', 'product_feature'])['iccs_used'].sum().reset_index()

# Analysis 4: By object_name
top_objects = df_all.groupby(['Date Range', 'object_name'])['iccs_used'].sum().reset_index()

# Recent trend summary (last 3 date tabs)
recent_tabs = sorted(df_all['Date Range'].unique())[-3:]
recent_data = df_all[df_all['Date Range'].isin(recent_tabs)]
summary_recent = recent_data.groupby(['product_vertical', 'product_feature'])['iccs_used'].sum().sort_values(ascending=False).reset_index()

# Export all to Excel
with pd.ExcelWriter("icc_usage_analysis_summary.xlsx") as writer:
    usage_trend.to_excel(writer, sheet_name="Usage_Trend", index=False)
    top_verticals.to_excel(writer, sheet_name="Top_Verticals", index=False)
    top_features.to_excel(writer, sheet_name="Top_Features", index=False)
    top_objects.to_excel(writer, sheet_name="Top_Objects", index=False)
    summary_recent.to_excel(writer, sheet_name="Recent_6W_Summary", index=False)

print("✅ All done! Output saved as 'icc_usage_analysis_summary.xlsx'")