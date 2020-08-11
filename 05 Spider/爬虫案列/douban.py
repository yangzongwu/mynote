from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 实例化一个浏览器对象（传入浏览器驱动程序）
def douban(ISBN):

    chrome_options = Options()

    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = "chromedriver.exe"  # 手动指定使用的浏览器位置

    bro = webdriver.Chrome(options=chrome_options)

    #bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    url='https://search.douban.com/book/subject_search?search_text='+str(ISBN)+'&cat=1001'
    bro.get(url)
    page_text = bro.page_source
    with open('../../test.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    btn = bro.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/a')
    btn.click()
    page_text = bro.page_source
    tree = etree.HTML(page_text)
    pic = tree.xpath('//*[@id="mainpic"]/a/img/@src')[0]
    name = tree.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    author = tree.xpath('//*[@id="info"]/span[1]/a/text()')[0]
    bro.quit()
    print(pic,name,author)
douban(9787115428028)
