import pandas as pd
df = pd.read_csv("../dataset/data_100_sample.csv")

print("6th  question: What other actionable insights can we gain by leveraging the TranStats dataset?")
print("the first popular destination")
df_6= df[[  "Origin","OriginCityName","Dest" ,"DestCityName","DepDelay", "FlightNum" ]]
dest_group_counts = df_6.groupby('DestCityName')['FlightNum'].nunique()
dest_group_counts = dest_group_counts.sort_values(ascending=False)
popular_dest = dest_group_counts.index[0]
print("first popular destination :", popular_dest, ", number of flights : ", dest_group_counts[popular_dest])