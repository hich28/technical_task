import pandas as pd


df = pd.read_csv("../dataset/data_100_sample.csv")


print("What airport has the 10th most delays?")
df_3 = df[[ "Origin","DepDelay" ]]
unique_airport_list= df_3["Origin"].unique() #get list of unique airports in the dataset
airp = [] #airport list
num_del =[] #number of delay list
for item in unique_airport_list:
    df_airports =  df_3[df_3["Origin"]==item] #select rows with same origin airport
    delay_list = df_airports["DepDelay"].values.tolist()
    count_del = 0
    for i in range(len(delay_list)):
        if delay_list[i]>0:
            count_del= count_del+1 #if the delay list is higher than 0 then this represnt a delay
    num_del.append(count_del)
    airp.append(item)
    my_dict = dict(zip(airp,num_del)) #create a dictionary {airport:number of delays}

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])  # Sort dictionary by values
# Access the 10th element (index 9) from the sorted list
if len(sorted_dict) >= 10:
    tenth_element = sorted_dict[9]
    print("Airport has the 10th most delays :",tenth_element)
else:
    print("The dictionary does not have 10 elements.")