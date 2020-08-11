from selenium import webdriver
from time import sleep
from lxml import etree
from selenium.webdriver.chrome.options import Options

option=Options()
option.add_argument('--headless')
bro=webdriver.Chrome(executable_path='chromedriver.exe', options=option)
url = 'http://opac.nlc.cn/F/N5QRKMT1IE9P17JM85Y58IP3CT4P5T5YQPA2KC1ERU5DG5YS5E-36940?find_code=ISB&request=&local_base=NLC01&func=find-b'
bro.get(url)
btn=bro.find_element_by_xpath('//*[@id="all_base"]')
btn.click()
btn=bro.find_element_by_xpath('//*[@id="find_code"]/option[16]')
btn.click()
ISBN=bro.find_element_by_xpath('//*[@id="reqterm"]')
ISBN.send_keys(9787115521637)
btn=bro.find_element_by_xpath('//*[@id="indexpage"]/form/div[2]/input')
btn.click()
sleep(1)
page_text = bro.page_source
tree = etree.HTML(page_text)
name_author=tree.xpath('//*[@id="td"]/tbody/tr[4]/td[2]/a/text()')[0]
[name,author]=name_author.split('/')
publisher=tree.xpath('//*[@id="td"]/tbody/tr[5]/td[2]/a/text()')[0]
abstract=tree.xpath('//*[@id="td"]/tbody/tr[10]/td[2]/text()')[0].strip()
print(name)
print(author)
print(publisher)
print(abstract)

bro.quit()