from fredapi import Fred

# add the API keys
def get_keys():
    api_kwarg = {}
    with open('fredapi.txt', 'r') as f:
        hold_lines = f.read().splitlines()

    for each in hold_lines:
        api_name, api_key_val = each.split('=')
        api_kwarg[api_name] = api_key_val
    return api_kwarg


api_kwarg = get_keys()

# init Fred
fred = Fred(api_key=api_kwarg['fred'])

# try GDP
data = fred.get_series_latest_release('GDP')
print(data.tail())