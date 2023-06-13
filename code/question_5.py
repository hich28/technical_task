import pandas as pd


df = pd.read_csv("../dataset/data_100_sample.csv")

print(" What is the 10th most flown route?")
df_5= df[[  "Origin","OriginCityName","Dest" ,"DestCityName","DepDelay", "FlightNum" ]]
df_5["route"] = df_5['Origin'].astype(str) +"-"+ df_5["Dest"]
rout_group_counts = df_5.groupby('route')['FlightNum'].nunique()
rout_group_counts=  rout_group_counts.sort_values(ascending=False)
tenth_grp =  rout_group_counts.index[9]
print("10th most flown route : ",tenth_grp, " number of flights : ", rout_group_counts[tenth_grp] )
