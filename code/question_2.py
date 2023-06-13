import pandas as pd


df = pd.read_csv("../dataset/data_100_sample.csv")


print("What carrier has flown the 3rd most number of flights? How many? " )
# vc_list=  df["Carrier"].value_counts().index.tolist()
# vc_values = df["Carrier"].value_counts().values.tolist()
# print("Carrier has flown the 3rd most number of flights : ",vc_list[2],  " number of flights: ", vc_values[2])
carrier_group_counts = df.groupby('Carrier')['FlightNum'].nunique()
carrier_group_counts = carrier_group_counts.sort_values(ascending=False)
print(carrier_group_counts)
third_carrier = carrier_group_counts.index[2]
print("Carrier has flown the 3rd most number of flights : ",third_carrier,  " number of flights: ", carrier_group_counts[third_carrier])