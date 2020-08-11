# selenium
* 为什么用selenium
    * 便捷的获取网站中动态加载的数据
    * 实现模拟登录  
* 什么是selenium模块
    * 基于浏览器自动化的一个模块
* 环境
    * 安装 pip install selenium
    * 下载浏览器驱动程序 https://chromedriver.storage.googleapis.com/index.html
    * 实例化一个对象
    * 编写基于浏览器自动化的操作代码
```python
from selenium import webdriver
from lxml import etree
import time
# 实例化一个浏览器对象（传入浏览器驱动程序）
bro=webdriver.Chrome(executable_path='爬虫案列/chromedriver.exe')
# 让浏览器发起一个指定的url对应的请求
bro.get('http://125.35.6.84:81/xk/')
# 获取浏览器当前页面的页面源码数据
page_text=bro.page_source
#解析企业名称
tree=etree.HTML(page_text)
li_list=tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name=li.xpath('./dl/@title')[0]
    print(name)
time.sleep(5)
bro.quit()
```

# selenium 基于浏览器自动化的操作代码
* 发起请求: get(url)
* 标签定位: find
* 标签交互:  send_key('xxx')
* 执行js程序: excute_stript('jscode')
* 前进，后退: back(),forward()
* 关闭浏览器: quit()
```python
from selenium import webdriver
from time import sleep
bro=webdriver.Chrome(executable_path='爬虫案列/chromedriver.exe')
bro.get('http://www.taobao.com')
search_input=bro.find_element_by_id('q')
search_input.send_keys('Iphone')
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(1)
btn=bro.find_element_by_css_selector('.btn-search')
btn.click()

bro.get('http://www.baidu.com')
sleep(2)
bro.back()
sleep(1)
bro.forward()
sleep(5)
bro.quit()
```
# iframe 处理
* 如果定位的标签存在于iframe标签中，则必须通过bro.switch_to.frame('id')
* 动作链：ActionChains
    * from selenium.webdriver import ActionChains
    * 实例化 action=ActionChains(bro)
    * 操作
```python
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
bro=webdriver.Chrome(executable_path='爬虫案列/chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#div=bro.find_element_by_id('draggable')
# 如果定位的标签存在于iframe标签中，则必须通过如下操作
bro.switch_to.frame('iframeResult')#切换标签的作用域
div=bro.find_element_by_id('draggable')
#动作链
action=ActionChains(bro)
action.click_and_hold(div)
for i in range(5):
    #perform立即执行
    action.move_by_offset(17,0).perform()
    sleep(0.3)
action.release()
bro.quit()
```

# selenium 模拟QQ空间登录
```python
from selenium import webdriver
from time import sleep
bro=webdriver.Chrome(executable_path='爬虫案列/chromedriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag=bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tg=bro.find_element_by_id('u')
password_tag=bro.find_element_by_id('p')
userName_tg.send_keys('xxxx')
password_tag.send_keys('xxxxx')
btn=bro.find_element_by_id('login_button')
btn.click()
sleep(3)
bro.quit()
```

# 无可视化界面（无头浏览器）+规避风险
```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 如何规避染个selenium规避检测
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
bro=webdriver.Chrome(executable_path='爬虫案列/chromedriver.exe',chrome_options=chrome_options,options=option)
bro.get('https://www.baidu.com/')# phantomJs

print(bro.page_source)
sleep(2)
bro.quit()
```
