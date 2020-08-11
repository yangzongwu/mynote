import requests
from lxml import etree

'''
def ipFinder(ip):
    url='https://iplocation.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    data = {'ip': ip}
    response = requests.get(url=url,params=data,headers=headers)
    try:
        page_text=response.text
        soup = BeautifulSoup(page_text, 'lxml')
        ip = soup.find('span', class_='country_name').text
    except:
        ip='None'
    print(ip)
'''


def ipcheck(ip):
    url='https://www.ip.cn/?ip='+ip
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    data=ip
    response = requests.get(url=url,params=ip,headers=headers)
    if not response:
        print(1)
    page_text=response.text
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    try:
        ip_name = tree.xpath('//div[@id="result"]/div/p[3]/code/text()')[0]
        ip_name=ip_name.split(',')[-1]
    except:
        ip_name='local host'
    print(ip_name)
    return ip_name

ipcheck('112.13.60.66 ')