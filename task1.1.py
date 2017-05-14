# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv('./data/JData_Action.csv')
user_data = pd.read_csv('./data/raw/JData_User.csv')

user_indexs = []
def dropTooMuchAction(df1,df2):
    counts = df1.groupby('user_id').count()['time'].values
    for i in np.arange(counts.size):
        if counts[i]>2500:
            user_indexs.append(i + 200001.0)
    for it in df1.index:
        if df1.ix[it].user_id in user_indexs:
            df1.drop(df1.index[it])
    for it2 in df2.index:
        if df2.ix[it2].user_id in user_indexs:
            df2.drop(df2.index[it2])
    df1.to_csv('./data/JData_Action_AfterDrop.csv',index=False)
    df2.to_csv('./data/JData_User_AfterDrop.csv',index=False)

dropTooMuchAction(data,user_data)

