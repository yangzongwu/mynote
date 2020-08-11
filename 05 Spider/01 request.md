# requests模块
python中原生的一款基于网路请求的模块，功能强大，简单便捷，效率极高
* 作用：模拟浏览器发请求
* 如何使用（requests编码流程）：
    * 指定url
    * 发起请求
    * 获取响应数据
    * 持久化存储
* 环境安装
    ```
    pip install requests
    ```

### 几个项目案列
* 案列一 爬取sogou首页的页面数据  
    * 基本用法，存储txt文档
* 案列二 request 网页采集器  
    * UA检测与伪装，headers设定
    * 带参爬虫
    * get请求
* 案列三 破解百度翻译  
    * 动态加载数据，ajax动态抓取url
    * post 请求（携带了参数）
    * 响应数据是一组json数据
* 案列四 豆瓣电影爬取  
    * 动态加载数据，ajax动态抓取url
    * 爬虫url参数设定
* 案列五 肯德基餐厅位置爬虫  
* 案列六 药监总局相关数据爬虫  
    * 动态加载数据，数据通过Ajax动态请求到的，而不是首页的url
    * 详情页的数据也是Ajax动态加载的数据
    * 详情页的url参数id通过首页的参数获得
    * 分页处理
### 案列一 爬取sogou首页的页面数据
```python
import requests
if __name__=="__main__":
# 指定url
    url="https://www.sogou.com/"
# 发起请求
    response=requests.get(url=url)
# 获取响应数据,.text返回的是字符串形式的响应数据
    page_text=response.text
# 持久化存储
    with open('./sogo.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
```

### 案列二 request 网页采集器
UA 检测： 门户网站的服务器会检查对应的载体身份标识，如果检测到请求的载体身份标识位某一款浏览器，说明该请求是一个正常请求
但是如果检查到请求的载体不是基于某一款浏览器的，则表示该请求位不正常的请求，服务器可能拒绝  
UA User-Agent(请求载体的身份标识)  
```python
import requests
if __name__=='__main__':
    #UA伪装
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    #https://www.sogou.com/web?query=dog
    url="https://www.sogou.com/web"
    # 处理url携带的参数：封装的到字典中
    kw=input('enter a word')
    param={'query':kw}
    # 对指定的url发起的请求对应url是携带参数的
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    file_name=kw+'.html'
    with open(file_name,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_name," 保持成功")
```

### 案列三 破解百度翻译
* post 请求（携带了参数）
* 响应数据是一组json数据
```python
import requests
import json
if __name__=='__main__':
    url='https://fanyi.baidu.com/sug'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    word=input('enter a word')
    data={'kw':word}
    response=requests.post(url=url,data=data,headers=headers)
    dict_obj=response.json()#返回的是obj,如果确认响应的是json类型的采用
    fileName=word+'.json'
    fp=open(fileName,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False)
    print("Done!")
```

### 案列四 豆瓣电影爬取
```python
import requests
import json
if __name__=='__main__':
    url="https://movie.douban.com/j/chart/top_list"
    params={
        'type': '11',
        'interval_id': '100:90',
        'action':'',
        'start': '0',#从库中第几部开始取
        'limit': '20',#一次取多少个
    }
    #UA伪装
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    response=requests.get(url=url,params=params,headers=headers)
    list_data=response.json()
    fp=open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('Done!')
```

### 案列五 肯德基餐厅位置爬虫
```python
import requests
import json
if __name__=='__main__':
    #UA伪装
    url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    params={
        'cname':'',
        'pid':'',
        'keyword': '北京',
        'pageIndex': 1,
        'pageSize': 100000
    }
    reponse=requests.get(url=url,params=params,headers=headers)
    data_list=reponse.text
    data_json=json.loads(data_list)
    fp = open('./KFC.json', 'w', encoding='utf-8')
    json.dump(data_json, fp=fp, ensure_ascii=False)
    print('Done!')
```

### 案列六 药监总局相关数据爬虫
* 动态加载数据
* 首页中对应的企业信息数据是同通过ajax动态请求到的
* 通过url观察，url域名都是一样的，只有携带的参数不一样，参数可以从首页对应的ajax里面字符串加载
* 详情页的数据也是Ajax动态加载的数据
* 观察后发现所有的POST请求的url都是一样的，只有参数id不同
* 分页
```python
import requests
import json
if __name__=='__main__':
    # 批量获取id
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []
    for page in range(1,6):
        page=str(page)
        data={
            'on': 'true',
            'page': page,
            'pageSize': 15,
            'productName':'',
            'conditionType': 1,
            'applyname':'',
            'applysn':'',
        }
        json_ids=requests.post(url=url,headers=headers,params=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    all_data_list=[]
    # 获取企业详情数据
    post_url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data={
            'id':id
        }
        detail_json=requests.post(url=post_url,data=data,headers=headers).json()
        all_data_list.append(detail_json)

    # 存储
    fp=open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('Done')
```