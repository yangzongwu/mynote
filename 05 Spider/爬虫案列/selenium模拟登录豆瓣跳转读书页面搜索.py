from selenium import webdriver
from time import sleep
from lxml import etree


bro = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://accounts.douban.com/passport/login?'
bro.get(url)
btn=bro.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]')
btn.click()
userName_tg=bro.find_element_by_id('username')
password_tag=bro.find_element_by_id('password')
userName_tg.send_keys('xxx')
password_tag.send_keys('xxx')
btn=bro.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a')
btn.click()
sleep(1)
btn=bro.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[4]/ul/li[2]/a')
btn.click()
bro.switch_to.window(bro.window_handles[1])
sleep(1)
ISBN=bro.find_element_by_xpath('//*[@id="inp-query"]')
ISBN.send_keys('9787115428028')
sleep(3)
btn=bro.find_element_by_xpath('//*[@id="db-nav-book"]/div[1]/div/div[2]/form/fieldset/div[2]/input')
btn.click()
sleep(1)
btn=bro.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/a')
btn.click()
sleep(2)
page_text = bro.page_source
tree = etree.HTML(page_text)
pic = tree.xpath('//*[@id="mainpic"]/a/img/@src')[0]
name = tree.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
author = tree.xpath('//*[@id="info"]/span[1]/a/text()')[0]
print(pic,name,author)
bro.quit()

