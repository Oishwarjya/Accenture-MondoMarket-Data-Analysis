# pip install pandas
# pip install pandas-profiling
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_excel('competitor_daily_sales.xlsx', error_bad_lines=False)
df2 = pd.read_excel('competitor_monthly_costs.xlsx', error_bad_lines=False)
print(df)

#Generate a report
profile = ProfileReport(df2)
profile.to_file(output_file="monthly_costs.html")

profile = ProfileReport(df)
profile.to_file(output_file="daily_sales.html")