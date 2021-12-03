# pip install pandas
# pip install pandas-profiling
import pandas as pd
from pandas_profiling import ProfileReport

# df is a variable (anything can be used) for data format (like a cursor)
df = pd.read_excel('competitor_daily_sales.xlsx', error_bad_lines=False)
df2 = pd.read_excel('competitor_monthly_costs.xlsx', error_bad_lines=False)
df3 = pd.read_excel('high_priority_usage_data.xlsx', error_bad_lines=False)

#Generate a report
profile = ProfileReport(df2)
profile.to_file(output_file="monthly_costs.html")

profile = ProfileReport(df)
profile.to_file(output_file="daily_sales.html")

profile = ProfileReport(df3)
profile.to_file(output_file="issues.html")