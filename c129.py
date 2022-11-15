import pandas as pd
df = pd.read_csv("project2_output.csv")
df.head()
df.dtypes

df = df.dropna()
df.dtypes

df["radius"] = 0.102763*df["radius"]
df['mass']=df['mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["mass"] = 0.000954588*df["mass"]


df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.head()
df.reset_index(drop=True,inplace=True)

df.to_csv("unit_converted_stars.csv")