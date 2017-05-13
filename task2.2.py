# -*- coding: utf-8 -*-
import pandas as pd


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


count_view_sku = {}
def get_view(df):
    global count_view_sku
    count_view_sku.update({df['sku_id'].iat[0] : df.shape[0]})
    
data[data.type!=4].groupby(['sku_id']).apply(get_view)

count_shop_sku = {}
def get_shop(df):
    global count_shop_sku
    count_shop_sku.update({df['sku_id'].iat[0] : df.shape[0]})
data[data.type == 4].groupby(['sku_id']).apply(get_shop)

T_sku = pd.DataFrame(T_sku.items(), columns=['sku_id','t_shop'])
count_view_sku =  pd.DataFrame(count_view_sku.items(), columns=['sku_id','view_count'])
count_shop_sku =  pd.DataFrame(count_shop_sku.items(), columns=['sku_id','shop_count'])
find_user = pd.merge(count_view_sku, count_shop_sku, 
                      on = 'sku_id',
                      how = 'left')
find_user = pd.merge(find_user, T_sku, on='sku_id', how='left')
find_user['view2shaop_rate'] = find_user['shop_count']/find_user['view_count']
find_user.to_csv('./data/find_user.csv', index=False)