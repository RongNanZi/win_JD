# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv('./data/JData_Action.csv')
data['time'] = data['time'].apply(pd.to_datetime)

T_one_sku_and_users = []
T_sku = {}
def get_T(df):
    global T_one_sku_and_users
    if df.shape[0] == 1:
        T_one_sku_and_users.append(35)
    else:
        df = df.sort('time',ascending=True)
        times = [pd.Timestamp(item).date() for item in df['time'].values]
        start = times[0]
        t = []
        for stamp in times[1:]:
            delta = stamp - start
            t.append(delta.days)
            start = stamp
        T_one_sku_and_users.append(sum(t)/len(t))
                        
def get_shopT(df):
    global T_one_sku_and_users
    global T_sku
    df.groupby(['user_id']).apply(get_T)
    temp = sum(T_one_sku_and_users)/len(T_one_sku_and_users)
    T_sku.update({df['sku_id'].iat[0] : temp})
    T_one_sku_and_users = []
    
    
data[data.type == 4].groupby(['sku_id']).apply(get_shopT)



T_sku = np.asarray(T_sku)
T_sku.dump('./data/T_shop_sku.dic')