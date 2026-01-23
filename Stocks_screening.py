import pandas as pd

# Load your dataset (replace with real data source)
df = pd.read_excel("/Users/goels2/Desktop/Business/Trading/Ticker_data/ticker_fy25/Performance_Screening_20_07_2025.xlsx")

 
# Filter criteria
filtered_df = df[
    (df['RSI Exponential ‚Äì 14D'] > 30) & (df['RSI Exponential ‚Äì 14D'] < 60) &  # Not overbought/oversold
    (df['% From Lower Bollinger Band'] < 20) &  # Closer to support
    (df['1M Return'] > 0) &  # Some short-term strength
    (df['6M Return'] > 0) &
    (df['5Y Historical EPS Growth'] > 5) &  # Strong fundamentals
    (df['5Y Hist Op. Cash Flow Growth'] > 5) &
    (df['5Y Historical Revenue Growth'] > 5)
]

# Sort by momentum and fundamentals
filtered_df = filtered_df.sort_values(
    by=['1M Return', '6M Return', '5Y Historical EPS Growth'],
    ascending=[False, False, False]
)

# Select top candidates
top_candidate = filtered_df[['Name', 'Ticker', 'Close Price', '1M Return', '6M Return',
                              'RSI Exponential ‚Äì 14D', '% From Lower Bollinger Band',
                              '5Y Historical EPS Growth', '5Y Historical Revenue Growth']].head(10)

print("Top Swing Trade Candidates (1–2 Months):")
print(top_candidate)