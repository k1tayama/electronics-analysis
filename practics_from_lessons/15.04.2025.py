import pandas as pd 

df = pd.read_csv("students.csv")
df = df.tail(5)
print(df.describe())
# print(df.isna()) # посмотреть пропуски (true - пропуск)
# print(df.isna().sum()) #посмотреть пропуски по сумме 
df["physics"] = df['physics'].astype(str).str.replace('%', '') # заменяем в строке % на ""
df['physics'] = df['physics'].astype(float)

df['attendance'] = df['attendance'].astype(float).apply(lambda x: x*100 if x > 1 else x)
df['city'] = df['city'].fillna("Unknow") # заполнить пропуски
df['project_score'] = df['project_score'].fillna(df['project_score'].mean())

df['best_subject'] = df[['math', 'physics', 'cs']].idxmax(axis=1)

df['grade'] = df['average'].apply(lambda x: "a" if x >= 85 else('b' if x>=70 else "c"))

df_sorted = df.sort_values(by=['group', 'average'], ascending=[True, False])

df.groupby(['group', 'best_subject'])['average'].mean()