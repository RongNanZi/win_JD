import pandas as pd

data_path = './data/raw/'
file_names = ['JData_Action_201602.csv','JData_Action_201603.csv','JData_Action_201604.csv']

csv_datas = []
for f_name in file_names:
	data = pd.read_csv(data_path+f_name, encoding='gbk')
	csv_datas.append(data.drop_duplicates(subset=['user_id','sku_id','time']))
merge_data = pd.concat(csv_datas, 0, ignore_index=False)
merge_data.to_csv('./data/JData_Action.csv', index=False)
	
