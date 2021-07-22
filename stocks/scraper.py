import requests
import pandas as pd
import datetime


def get_data(ticker, years) -> pd.DataFrame:
    headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    dt= datetime.datetime.now()
    past_date = datetime.datetime(year=dt.year-years, month=dt.month, day=dt.day)
    payload = {
        'formatted': 'true',
        'crumb': 'J2oUJNHQwXU',
        'lang': 'en-GB',
        'region': 'GB',
        'includeAdjustedClose': 'true',
        'interval': '1d',
        'period1': '%s' %int(past_date.timestamp()),
        'period2': '%s' %int(dt.timestamp()),
        'events': 'div|split',
        'useYfid': 'true',
        'corsDomain': 'uk.finance.yahoo.com'}
    url = 'https://query2.finance.yahoo.com/v8/finance/chart/{0}'.format(ticker)
    jsonData = requests.get(url, headers=headers, params=payload).json()
    result = jsonData['chart']['result'][0]
    indicators = result['indicators']
    rows = {'timestamp':result['timestamp']}
    rows.update(indicators['adjclose'][0])
    rows.update(indicators['quote'][0])
    df = pd.DataFrame(rows)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
 
# if __name__ == "__main__":
#     df = get_data('SPCE', 2)
  
    #df.to_csv("history_spce.csv")
