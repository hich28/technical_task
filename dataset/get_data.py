import pandas as pd


df = pd.read_csv("../dataset/On_Time_On_Time_Performance_2017_1.csv")
df =  df[["DayOfWeek","FlightDate","UniqueCarrier","AirlineID","Carrier", "TailNum", "FlightNum",
          "OriginAirportID", "OriginAirportSeqID", "OriginCityMarketID", "Origin", "OriginCityName","OriginState","OriginStateFips",
          "OriginStateName", "OriginWac","DestAirportID", "DestAirportSeqID", "DestCityMarketID", "Dest", "DestCityName",
          "DestState", "DestStateFips","DestStateName","DestWac", "CRSDepTime", "DepTime","DepDelay","DepDelayMinutes",
          "DepDel15", "DepartureDelayGroups", "DepTimeBlk", "TaxiOut", "WheelsOff","WheelsOn", "TaxiIn", "CRSArrTime",
          "ArrDelay", "ArrDelayMinutes", "ArrDel15", "ArrivalDelayGroups", "ArrTimeBlk", "Cancelled","Diverted",
          "CRSElapsedTime", "ActualElapsedTime", "AirTime", "Flights", "Distance","DistanceGroup"]]
df = df.sample(n=200,random_state=22)
df.to_csv("../dataset/data_100_sample.csv")