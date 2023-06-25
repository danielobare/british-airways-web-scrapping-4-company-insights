import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('BA_reviews_1.csv')

print (df.head())

profile = ProfileReport(df, title - 'BA Review Analysis')

profile.to_file('BA_Review_Analysis.html')

