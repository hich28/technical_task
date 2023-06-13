import pandas as pd


df = pd.read_csv("../dataset/data_100_sample.csv")


print("What is the second most popular day of the week to travel? Why?")
flight_by_day_counts= df.groupby('DayOfWeek')['FlightNum'].nunique() #get subsets of data grouped by day of the week
sorted_number_of_flights_per_day= flight_by_day_counts.sort_values(ascending=False)
second_most_pop_day= sorted_number_of_flights_per_day.index[1] # Find the second group with the most number of elements
print("Number of flights per day ",sorted_number_of_flights_per_day) #number of flights per day of week
print("second most popular day of the week to travel is : ",second_most_pop_day, "why ? number of flights : ", flight_by_day_counts[second_most_pop_day] )
