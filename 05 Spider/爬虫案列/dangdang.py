from selenium import webdriver
from time import sleep
from lxml import etree
import requests

def dangdang(ISBN):
    url = 'http://search.dangdang.com/?key=' + str(ISBN) + '&act=input&sort_type=sort_sale_amt_desc#J_tab'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list=tree.xpath('//*[@id="component_59"]/li')
    result=[]
    for li in li_list[:5]:
        detail_url=li.xpath('./a/@href')[0]
        print(detail_url)
        bro = webdriver.Chrome(executable_path='chromedriver.exe')
        bro.get(detail_url)
        sleep(0.3)
        btn = bro.find_element_by_xpath('//*[@id="comm_num_down"]')
        btn.click()
        sleep(0.2)
        detail_page_text = bro.page_source
        with open('dd.html', 'w', encoding='utf-8') as fp:
            fp.write(detail_page_text)
        detail_page_tree = etree.HTML(detail_page_text)
        good_price=detail_page_tree.xpath('//*[@id="dd-price"]/text()')[0]
        good_price_unit = detail_page_tree.xpath('//*[@id="dd-price"]/span/text()')[0]
        good_num_comment=detail_page_tree.xpath('//*[@id="comm_num_down"]/text()')[0]
        if int(good_num_comment)>=10000:
            good_num_comment=str(round(int(good_num_comment)/10000,0))+'万'
        good_comment_rate = detail_page_tree.xpath('//*[@id="comment_all"]/div[1]/div[1]/div/div/span[2]/text()')[0]
        good_comment_rate=str(round(float(good_comment_rate),1))+'%'
        res = {
            'good_price': good_price,
            'good_price_unit': good_price_unit,
            'good_from': 'Dangdang',
            'good_url': detail_url,
            'good_comment_rate': good_comment_rate,
            'good_num_comment': good_num_comment,
        }
        result.append(res)
        bro.quit()

