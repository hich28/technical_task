import pandas as pd
df = pd.read_csv("../dataset/data_100_sample.csv")
print("Question: What is the 2 nd most delayed route of the flights operated by ‘Pacific Airways’? " )
df = df.sort_values(by=['DepDelay'], ascending=False)
df_n = df[[ "Origin","OriginCityName","Dest" ,"DestCityName","DepDelay" ]]
print("Second most delayed route :")
print(df_n.iloc[[1]] )
