import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display


pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

url = 'https://tw.stock.yahoo.com/rank/change-up'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

stock_rankings = []

k = 1
for i in soup.find_all('li', class_="List(n)"): # limit=2(option)
    stock_name = i.find('div', class_='Lh(20px) Fw(600) Fz(16px) Ell').text
    stock_number = i.find('span', class_='Fz(14px) C(#979ba7) Ell').text
    final_price = i.find('span', class_='Jc(fe) Fw(600) C(#fff) Px(6px) Py(2px) Bdrs(4px) Bgc($c-trend-up)')
    if not final_price:
        final_price = i.find('span', class_='Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)')
    final_price = final_price.text
    ups_and_downs = i.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-up)')[0].text
    ups_and_downs_per = i.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-up)')[1].text
    highest = i.find_all('span', class_='Jc(fe)')[0].text
    lowest = i.find_all('span', class_='Jc(fe)')[1].text
    spread = i.find_all('span', class_='Jc(fe)')[2].text
    volume = i.find_all('span', class_='Jc(fe)')[3].text
    transaction_value = i.find_all('span', class_='Jc(fe)')[4].text

    stock_infos = {
        'stock_name': stock_name,
        'stock_number': stock_number,
        'final_price': final_price,
        'ups_and_downs': ups_and_downs,
        'ups_and_downs_per': ups_and_downs_per,
        'highest': highest,
        'lowest': lowest,
        'spread': spread,
        'volume': volume,
        'transaction_value': transaction_value,
    }
    # print(stock_infos)
    stock_rankings.append(stock_infos)
    # print('='*50)

# print(stock_rankings)
df = pd.DataFrame(data=stock_rankings)
df_rename = df.rename(
    columns={
        'stock_name':'股名',
        'stock_number':'股號',
        'final_price':'成交價',
        'ups_and_downs':'漲跌',
        'ups_and_downs_per':'漲跌幅(%)',
        'highest':'最高',
        'lowest':'最低',
        'spread':'價差',
        'volume':'成交量(張)',
        'transaction_value':'成交值(億)',
    }
)
print(df_rename)
# display(df_rename)
df_rename.to_csv('df_renames.csv') # 存成csv