# -*- coding: utf-8 -*-
import pandas as pd

data_path = './data/'
data = pd.read_csv('./data/JData_Action.csv')
data['time'] = data['time'].apply(pd.to_datetime)

user2sku_view = []
def get_user2sku_view(df):
    global user2sku_view
    temp = [df['user_id'].iat[0], df['sku_id'].iat[0], df.shape[0]]
    
    times = [pd.Timestamp(item).date() for item in df['time'].values]
    df[['time']] = pd.DataFrame(times, columns=['time'])
    temp.append(df.drop_duplicates(['time']).shape[0])
    user2sku_view.append(temp)
    
data[data.type != 4].groupby(['user_id','sku_id']).apply(get_user2sku_view)
u2sv = pd.DataFrame(user2sku_view, cloumns=['user_id','sku_id', 'view_count', 'view_days']).drop_duplicates(['user_id','sku_id', 'view_count','view_days'])

user2sku_shop = []
def get_user2sku_shop(df):
    global user2sku_shop
    temp = [df['user_id'].iat[0], df['sku_id'].iat[0], df.shape[0]]
    
    times = [pd.Timestamp(item).date() for item in df['time'].values]
    df[['time']] = pd.DataFrame(times, columns=['time'])
    temp.append(df.drop_duplicates(['time']).shape[0])
    user2sku_shop.append(temp)
    
data[data.type == 4].groupby(['user_id','sku_id']).apply(get_user2sku_shop)
u2ss = pd.DataFrame(user2sku_shop, cloumns=['user_id','sku_id', 'shop_count', 'shop_days']).drop_duplicates(['user_id','sku_id', 'shop_count','shop_days'])

times = [pd.Timestamp(item).date() for item in data['time'].values]
data[['time']] = pd.DataFrame(times, columns=['time'])
final_day = times[-1]
user2sku_final = []
def get_user2sku_final(df):
    global user2sku_final
    global final_day
    operate_final_day = df[['time']].values[-1]
    dealta_day = (final_day - operate_final_day).days
    temp = [df['user_id'].iat[0], df['sku_id'].iat[0], dealta_day]
    user2sku_final.append(temp)
    
data.groupby(['user_id','sku_id']).apply(get_user2sku_final)
to_final_day = pd.DataFrame(user2sku_view, cloumns=['user_id','sku_id', 'final_operate']).drop_duplicates(['user_id','sku_id', 'final_operate'])

csv_data = pd.merg(u2sv, u2ss, on = ['user_id','sku_id'], how = 'left')
csv_data = pd.merg(csv_data, to_final_day, on = ['user_id','sku_id'], how = 'left')
csv_data.to_csv(data_path+'find_user_sku_action.csv') 