from lxml import html
import requests

cookies = {}  # Cookies insert here

headers = {}  # Headers insert here

response = requests.get('', headers=headers, cookies=cookies)  # Your CFN page

cfn = html.fromstring(response.content)
lp = cfn.xpath('//*[@id="wrapper"]/main/section[2]/div/div[2]/div[4]/div/div[1]/dl[2]/dd/text()')

print(lp[0])
