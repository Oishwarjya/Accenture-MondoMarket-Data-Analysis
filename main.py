# pip install pandas
# pip install pandas-profiling
import pandas as pd

df = pd.read_excel('competitor_daily_sales.xlsx', error_bad_lines=False)

print(df)