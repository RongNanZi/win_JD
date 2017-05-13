# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv('./data/JData_Action.csv')

all_counts = {}
def user2sku(df):
    view_counts = df.groupby('sku_id').count()['Unnamed: 0'].values
    most_count = max(view_counts)
    all_counts.update({df['user_id'].iat[0] : most_count})
    
data.groupby('user_id').apply(user2sku)

all_counts = np.asarray(all_counts)
all_counts.dump('./data/user2one_sku_most_count.dic')