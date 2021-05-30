import pandas as pd
df=pd.read_csv("Book1.csv")
def Logs(df):
    urls=df.Column9
    distinct=urls.value_counts()
    print("the total no of distinct urls:",len(distinct))
    for i in distinct:
        print(distinct[distinct==i].index.values," --->",i)
Logs(df)
