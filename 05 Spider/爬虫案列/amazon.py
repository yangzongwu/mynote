from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options

ISBN=9787115428028
option=Options()
option.add_argument('--headless')
bro=webdriver.Chrome(executable_path='chromedriver.exe', options=option)
url = 'https://www.amazon.cn/dp/B0719GSVJB/ref=sr_1_1?keywords='+str(ISBN)
bro.get(url)
page_text = bro.page_source
tree = etree.HTML(page_text)
img=tree.xpath('//*[@id="ebooksImgBlkFront"]/@src')[0]
rate=tree.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()')[0].split(' ')[0]
rate=round(float(rate)*20,1)
comment=tree.xpath('//*[@id="acrCustomerReviewText"]/text()')[0].split(' ')[0]
print(img)
print(rate)
print(comment)

bro.quit()