import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('BA_reviews_1.csv')

print (df.head())
