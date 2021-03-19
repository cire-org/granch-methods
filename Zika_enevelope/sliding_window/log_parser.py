import pandas as pd
import datetime

def variety_calculator(data):
	index_to_variety_dict = dict()
	# print(data.shape)
	for i in range(1, 1690):
		# print(data[str(i)].unique())
		# print(data[str(i)].nunique())
		index_to_variety_dict[i] = data[str(i)].nunique()
	return index_to_variety_dict
	# print("\n".join(str(sorted(index_to_variety_dict.items(), key=lambda x: x[1]))))
	# print(sorted(index_to_variety_dict.items(), key=lambda x: x[1]))
	# data.shape

start_time = datetime.datetime.now()
data_randic3d = pd.read_csv("logs/randic3dplot.csv") 
data_nandy = pd.read_csv("logs/nandyplot.csv") 

# data = pd.read_csv("logs/randic3dplot_bkp.csv") 
# data = data[0].str.split(',', expand=True)
# Preview the first 5 lines of the loaded data 
final_data = pd.DataFrame()
data_randic3d = pd.DataFrame(variety_calculator(data_randic3d).items(), columns=['index', 'randic3d'])
# final_data = data_randic3d
print(data_randic3d.shape)
data_nandy = pd.DataFrame(variety_calculator(data_nandy).items(), columns=['index', 'nandy'])
print(data_nandy.shape)
# # data_randic3d.merge(on)
# # newDF = pd.concat([data_randic3d, data_nandy], axis=1, join='inner')
final_data = pd.merge(data_randic3d, data_nandy, how='inner', on='index')
del data_randic3d
del data_nandy
data_jili = pd.read_csv("logs/jiliplot.csv") 
data_jili = pd.DataFrame(variety_calculator(data_jili).items(), columns=['index', 'jili'])
print(data_jili.shape)
final_data = pd.merge(final_data, data_jili, how='inner', on='index')
del data_jili
data_randic2d = pd.read_csv("logs/randic2dplot.csv")
data_randic2d = pd.DataFrame(variety_calculator(data_randic2d).items(), columns=['index', 'randic2d'])
print(data_randic2d.shape)
final_data = pd.merge(final_data, data_randic2d, how='inner', on='index')
del data_randic2d 
data_songtang = pd.read_csv("logs/songtangplot.csv") 
data_songtang = pd.DataFrame(variety_calculator(data_songtang).items(), columns=['index', 'songtang'])
print(data_songtang.shape)
final_data = pd.merge(final_data, data_songtang, how='inner', on='index')
del data_songtang
# print(data_randic3d.head())
# print(data_nandy.head())	
print(final_data.head())
final_data.to_csv('logs/final_data.csv')
# end_time = datetime.datetime.now()
# time_taken = end_time - start_time
# print('time taken (in microseconds) = ' + str(time_taken.microseconds))
# print('time taken (in seconds) = ' + str(time_taken.seconds))
# print(pd.DataFrame(variety_calculator(data_randic3d).items()).head())

