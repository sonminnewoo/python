import pandas as pd 

filename =  "../CSV/singer2.csv"
df = pd.read_csv(filename,index_col=None, encoding='CP949')
print(df)
df_sort1 = df.sort_values(by=['평균 키'], axis=0)
print(df_sort1)