# script to split our big data file into 60% test, 20% val, and 20% train
# following the original paper, we do the split based on time with no shuffling
import numpy as np
import pandas as pd
df = pd.read_csv("dataset_example/WindData/dataset/Windspeeds_Full_TestTrainVal.csv", header=None)

#get number of records in each split
train= int(0.6*df.shape[0])
val = int(0.2*df.shape[0])

#rename header variables
df.loc[:1,].replace(['DATE', 'ATMP', 'PRES', 'DEWP', "GST", "WSPD"], ['time', 'air_temperature', 'air_pressure_at_sea_level', 'dew_point_temperature', "max(wind_speed_of_gust PT10M)", "wind_speed"], inplace=True)
df.replace(np.NaN, 9999, inplace=True)
df = df.dropna()

#getting heading values in the right order
df = df.transpose()
df= df.sort_values(by=[0, 1], ascending=[True, True])
df = df.transpose()

#remove unnecessary headings
df.columns = [i for i in range(df.shape[1])] #TODO check new number of columns
df = df.drop(columns=[i for i in range(9,18)], axis = 1)

# reorder appropriate headings
tide = [i for i in range(0, 9)]
time = [i for i in range(72, 81)]
first = [i for i in range(18, 72)]
last = [i for i in range(81, 90)]
time.extend(first)
time.extend(tide)
time.extend(last)
df = df[time]

header = df.loc[:1,]
df_train = df.loc[2:train,]
df_val = df.loc[train+1:train+val,]
df_test = df.loc[train+val+1:,]

df_train = pd.concat([header,df_train])
df_val = pd.concat([header,df_val])
df_test = pd.concat([header,df_test])

#write out csv
df_train.to_csv("dataset_example/WindData/dataset/train/wind_data.csv", index=False, header=False)
df_val.to_csv("dataset_example/WindData/dataset/val/wind_data.csv", index=False, header=False)
df_test.to_csv("dataset_example/WindData/dataset/test/wind_data.csv", index=False, header=False)
