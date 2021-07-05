import requests
from bs4 import BeautifulSoup


url = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=6246238&Area=search&mdiv=403&oid=1_1&cid=index&kw=%E7%9B%9B%E9%A6%99%E7%8F%8D%E5%A0%85%E6%9E%9C%E7%BD%90'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

category_lists = []

for i in soup.find_all('div', class_="related_category"): # limit=2(option)
    product_brand_name = i.find('a', class_='webBrandLink').text.replace(' ', '')
    product_second_to_last = i.find_all('dl')[-2].find_all('dd')[-1].text
    product_first_to_last = i.find_all('dl')[-1].find_all('dd')[-1].text
    category_lists.append({
        'product_brand_name': product_brand_name,
        'product_second_to_last': product_second_to_last,
        'product_first_to_last': product_first_to_last,
    })
print(category_lists)