import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn-deep')

def get_all_dfs():
	# get csvs from data/KPIs
	get_csvs = os.listdir('data/Employment')
	# create and hold dfs of each
	all_dfs = {}
	cols = ['Date','Value']
	for each in get_csvs:
		all_dfs[each.split('.')[0]] = pd.read_csv('data/Employment/'+each, names=cols)
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
	plt.savefig('plots/Employment/'+title+'.png')
	plt.show()



all_dfs = get_all_dfs()

# Ready recession.csv
all_dfs['recession']['Date'] = pd.to_datetime(all_dfs['recession']['Date'])
all_dfs['recession']['Value'] = pd.to_datetime(all_dfs['recession']['Value'])

# Employment_categories = ['LNU02073395','CES0500000003','UNRATENSA','JTSJOL','JTSLDL','LNS13023653','NILFWJN','JTS1000JOL','ICSA','USGOOD','SRVPRD']

mega_df = all_dfs['JTSJOL']
mega_df = pd.merge(mega_df, all_dfs['JTS1000JOL'], on = 'Date', how = 'outer')
mega_df.rename(columns={u'Value_x': 'Job Openings Nonfarm', u'Value_y': 'Job Openings Private'}, inplace=True)
mega_df['Date'] = pd.to_datetime(mega_df['Date'])
plot_me_with_recession(mega_df, all_dfs['recession'], 'Job openings in Nonfarm and Private')

# mega_df = all_dfs['LNU02073395']
# mega_df = pd.merge(mega_df, all_dfs['CES0500000003'], on = 'Date', how = 'outer')
# mega_df['Date'] = pd.to_datetime(mega_df['Date'])
# mega_df.rename(columns={u'Value_x':'Unemployment Level', u'Value_y':'Avg Hourly Earnings Private sector'})
# plot_me_with_recession(all_dfs['ICSA'], all_dfs['recession'], 'Unemployment level and ')


mega_df = all_dfs['USGOOD']
mega_df = pd.merge(mega_df, all_dfs['SRVPRD'], on = 'Date', how = 'outer')
mega_df['Date'] = pd.to_datetime(mega_df['Date'])
mega_df.rename(columns={u'Value_x':'Goods producing employees', u'Value_y':'Service producing employees'}, inplace=True)
plot_me_with_recession(mega_df, all_dfs['recession'], 'Initial Claims')

mega_df = all_dfs['LNU02073395']
all_dfs['LNU02073395']['Date'] = pd.to_datetime(all_dfs['LNU02073395']['Date'])
mega_df.rename(columns={'Value':'Unemployment Level'}, inplace=True)
plot_me_with_recession(mega_df, all_dfs['recession'], 'Unemployment Level')

# mega_df = all_dfs['CES0500000003']
# all_dfs['CES0500000003']['Date'] = pd.to_datetime(all_dfs['CES0500000003']['Date'])
# mega_df.rename(columns={'Value':'Hourly Earnings Private Sector'})
# plot_me_with_recession(all_dfs['ICSA'], all_dfs['recession'], 'Hourly Earnings in Private Sector')

mega_df = all_dfs['ICSA']
all_dfs['ICSA']['Date'] = pd.to_datetime(all_dfs['ICSA']['Date'])
mega_df.rename(columns={'Value':'Initial Claims'}, inplace=True)
plot_me_with_recession(all_dfs['ICSA'], all_dfs['recession'], 'Initial Claims')

mega_df = all_dfs['JTSLDL']
all_dfs['JTSLDL']['Date'] = pd.to_datetime(all_dfs['JTSLDL']['Date'])
mega_df.rename(columns={'Value':'Initial Claims'}, inplace=True)
plot_me_with_recession(all_dfs['JTSLDL'], all_dfs['recession'], 'Layoffs')


mega_df = all_dfs['NILFWJN']
all_dfs['NILFWJN']['Date'] = pd.to_datetime(all_dfs['NILFWJN']['Date'])
mega_df.rename(columns={'Value':'Not working-needs job NOW'}, inplace=True)
plot_me_with_recession(all_dfs['NILFWJN'], all_dfs['recession'], 'Not working-Needs Job NOW')

mega_df = all_dfs['UNRATENSA']
all_dfs['UNRATENSA']['Date'] = pd.to_datetime(all_dfs['UNRATENSA']['Date'])
mega_df.rename(columns={'Value':'Unemployment Rate'}, inplace=True)
plot_me_with_recession(all_dfs['UNRATENSA'], all_dfs['recession'], 'Unemployment Rate-USA')
