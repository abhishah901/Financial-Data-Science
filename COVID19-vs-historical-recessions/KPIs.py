import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn-deep')

def get_all_dfs():
	# get csvs from data/KPIs
	get_csvs = os.listdir('data/KPI')
	# create and hold dfs of each
	all_dfs = {}
	cols = ['Date','Value']
	for each in get_csvs:
		all_dfs[each.split('.')[0]] = pd.read_csv('data/KPI/'+each, names=cols)
	return all_dfs


def print_dates(all_dfs):
	for k,v in all_dfs.items():
		print(k)
		print(v.head(2))
		print(v.tail(2))




# plotter func with recession
def plot_me_with_recession(df, recession_df, title = 'Plot'):
	df.plot('Date')
	for index, row in recession_df.iterrows():
		plt.axvspan(row['Date'],row['Value'], color = 'red', alpha = 0.2)
	plt.title(title)
	plt.savefig('plots/KPI/'+title+'.png')
	plt.show()



all_dfs = get_all_dfs()

# Ready recession.csv
all_dfs['recession']['Date'] = pd.to_datetime(all_dfs['recession']['Date'])
all_dfs['recession']['Value'] = pd.to_datetime(all_dfs['recession']['Value'])



# Prepare GDP(GDP) with GDP per capita(A939RC0Q052SBEA)
mega_df = all_dfs['GDP']
print(mega_df.columns)
mega_df = pd.merge(mega_df, all_dfs['A939RC0Q052SBEA'], on = 'Date', how = 'outer')
mega_df['Date'] = pd.to_datetime(mega_df['Date'])
mega_df.rename(columns={u'Value_x':'GDP',u'Value_y':'GDP per capita'}, inplace=True)
print(mega_df.columns)
plot_me_with_recession(mega_df,all_dfs['recession'],'GDP and GDP per capita during recessions')    


# Prepare Federal Government; Consumer Credit, Student Loans; Asset, Flow (FGCCSLQ027S)
all_dfs['FGCCSLQ027S']['Date'] = pd.to_datetime(all_dfs['FGCCSLQ027S']['Date'])
all_dfs['FGCCSLQ027S'].rename(columns={'Value':'Asset Flow'}, inplace=True)
plot_me_with_recession(all_dfs['FGCCSLQ027S'], all_dfs['recession'], 'Federal Government; Consumer Credit, Student Loans; Asset, Flow during Recessions')


# Prepare Exports: Value Goods for the United States  (XTEXVA01USM664S) 
all_dfs['XTEXVA01USM664S']['Date'] = pd.to_datetime(all_dfs['XTEXVA01USM664S']['Date'])
all_dfs['XTEXVA01USM664S'].rename(columns={u'Value':'Export: Value Goods'}, inplace=True)
plot_me_with_recession(all_dfs['XTEXVA01USM664S'], all_dfs['recession'], 'Exports-Value Goods for the United States')


# Prepare Effective Federal Funds Rate (FEDFUNDS) 
all_dfs['FEDFUNDS']['Date'] = pd.to_datetime(all_dfs['FEDFUNDS']['Date'])
all_dfs['FEDFUNDS'].rename(columns={'Value':'Federal Funds'}, inplace=True)
plot_me_with_recession(all_dfs['FEDFUNDS'], all_dfs['recession'], 'Effective Federal Funds Rate')


# Prepare Personal Consumption Expenditures (PCE)
all_dfs['PCE']['Date'] = pd.to_datetime(all_dfs['PCE']['Date'])
all_dfs['PCE'].rename(columns={'Value':'Personal Consumption Expenditures'}, inplace=True)
plot_me_with_recession(all_dfs['PCE'], all_dfs['recession'], 'Personal Consumption Expenditures')


# Prepare Commercial and Industrial Loans, All Commercial Banks (TOTCI)
all_dfs['TOTCI']['Date'] = pd.to_datetime(all_dfs['TOTCI']['Date'])
all_dfs['TOTCI'].rename(columns={'Value':'All Commercial Bank Loans '}, inplace=True)
plot_me_with_recession(all_dfs['TOTCI'], all_dfs['recession'], 'Commercial and Industrial Loans, All Commercial Banks')

