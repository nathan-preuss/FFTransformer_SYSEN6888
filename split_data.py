# script to split our big data file into 60% test, 20% val, and 20% train
# following the original paper, we do the split based on time with no shuffling
#TODO: eventually adjust model from hours ahead to year ahead forecasting
import pandas as pd
df = pd.read_csv("dataset_example/WindData/dataset/Windspeeds_Full_TestTrainVal.csv")
print(df.shape[0])

#get number of records in each split
train= int(0.6*df.shape[0])
val = int(0.2*df.shape[0])

#split df
df_train = df.loc[:train,]
df_val = df.loc[train:train+val,]
df_test = df.loc[train+val:,]

#write out csv
df_train.to_csv("dataset_example/WindData/dataset/train/wind_data.csv")
df_val.to_csv("dataset_example/WindData/dataset/val/wind_data.csv")
df_test.to_csv("dataset_example/WindData/dataset/test/wind_data.csv")
