# script to split our big data file into 60% test, 20% val, and 20% train
# following the original paper, we do the split based on time with no shuffling
#TODO: eventually adjust model from hours ahead to year ahead forecasting
import pandas as pd
df = pd.read_csv("dataset_example/WindData/dataset/Windspeeds_Full_TestTrainVal.csv", header=None)
print(df.shape[0])

#get number of records in each split
train= int(0.6*df.shape[0])
val = int(0.2*df.shape[0])

#split df
header = df.loc[:1,]
df_train = df.loc[2:train,]
df_val = df.loc[train+1:train+val,]
df_test = df.loc[train+val+1:,]

#rename header variables
header.replace(['DATE', 'ATMP', 'PRES', 'DEWP', "GST", "WSPD"], ['time', 'air_temperature', 'air_pressure_at_sea_level', 'dew_point_temperature', "max(wind_speed_of_gust PT10M)", "wind_speed"], inplace=True)

df_train = pd.concat([header,df_train])
df_val = pd.concat([header,df_val])
df_test = pd.concat([header,df_test])

#write out csv
df_train.to_csv("dataset_example/WindData/dataset/train/wind_data.csv", index=False, header=False)
df_val.to_csv("dataset_example/WindData/dataset/val/wind_data.csv", index=False, header=False)
df_test.to_csv("dataset_example/WindData/dataset/test/wind_data.csv", index=False, header=False)
