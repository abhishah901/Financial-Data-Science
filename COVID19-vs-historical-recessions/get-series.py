from fredapi import Fred

# add the API keys
def get_keys():
    api_kwarg = {}
    with open('apikeys.txt', 'r') as f:
        hold_lines = f.read().splitlines()
    for each in hold_lines:
        api_name, api_key_val = each.split('=')
        api_kwarg[api_name] = api_key_val
    return api_kwarg


api_kwarg = get_keys()

# init Fred
api_handler = Fred(api_key=api_kwarg['fred'])
def get_series(categories):
    for each in categories:
        hold_series = api_handler.get_series_latest_release(each)
        filename = 'data/'+each+'.csv'
        hold_series.to_csv(filename)
        print(each+' : ',len(hold_series))
        print('First and last rows:')
        print(hold_series.iloc[[0, -1]])


KPI_categories = ['XTEXVA01USM664S','GDP','PCE','CES0500000003','A939RC0Q052SBEA','FGCCSLQ027S','TOTCI','FEDFUNDS']


get_series(KPI_categories)

#REFERENCES

# Get details of all the series by add the series categories at https://fred.stlouisfed.org/series/<your category>

# To find the categories
#KPIs of an Economy/Recession
#Exports: Value Goods for the United States (XTEXVA01USM664S) 
#Average Hourly Earnings of All Employees, Total Private (CES0500000003) 
#Gross domestic product per capita (A939RC0Q052SBEA) 
#Federal Government; Consumer Credit, Student Loans; Asset, Flow (FGCCSLQ027S) 
#Commercial and Industrial Loans, All Commercial Banks (TOTCI) 
#Personal Consumption Expenditures (PCE)
#Effective Federal Funds Rate (FEDFUNDS) 
#Gross Domestic Product (GDP)  

#Employment
#Employment Level - Foreign Born (LNU02073395)
#Unemployment Rate (UNRATENSA) 
#Job Openings: Total Nonfarm (JTSJOL) 
#Layoffs and Discharges: Total Nonfarm (JTSLDL) 
#Unemployment Level - Job Losers on Layoff (LNS13023653) 
#Not in Labor Force - Want a Job Now (NILFWJN) 
#Job Losers on Layoff as a Percent of Total Unemployed (LNS13023654) 
#Job Openings: Total Private (JTS1000JOL) 
#Initial Claims (ICSA) 
#All Employees, Goods-Producing (USGOOD) 
#All Employees, Service-Providing (SRVPRD) 
