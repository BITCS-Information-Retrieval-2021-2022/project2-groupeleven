import re
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import sys
import pymongo
import traceback


# 用学者名称在semantic scholar查询，根据论文是否匹配建立aminer网页和semantic scholar网页之间的匹配，爬取semantic scholar网页的数据
def s_search(name, papers):

    # 用学者名称在semantic scholar查询
    url = 'https://www.semanticscholar.org/api/1/search'
    name = name.replace('\"', '')
    query = f'''{{"queryString": "{name}",
    "page": 1,
    "pageSize": 3,
    "sort": "relevance",
    "authors": [],
    "coAuthors": [],
    "venues": [],
    "yearFilter": null,
    "requireViewablePdf": false,
    "publicationTypes": [],
    "externalContentTypes": [],
    "fieldsOfStudy": [],
    "useFallbackRankerService": false,
    "useFallbackSearchCluster": false,
    "hydrateWithDdb": true,
    "includeTldrs": true,
    "performTitleMatch": true,
    "includeBadges": true,
    "tldrModelVersion": "v2.0.0",
    "getQuerySuggestions": false
    }}'''
    while 1:
        try:
            res = requests.post(url, json=json.loads(query)).json()
            break
        except requests.exceptions.ConnectionError as e:
            print('error_name:', e.__class__.__name__)
            print('error:', e)
    matchedAuthors = res.get("matchedAuthors", [])

    # 筛选查询结果小于等于3名学者，根据论文是否匹配建立aminer网页和semantic scholar网页之间的匹配，爬取semantic scholar网页的数据
    if len(matchedAuthors)>3:
        matchedAuthors = matchedAuthors[:3]
    for i in matchedAuthors:
        id = i.get("id")
        print("id:", id)
        response = s_get_response(id)
        for i in response["papers"]:
            for j in papers:
                if i.lower() == j.lower():
                    print("matching success")
                    return response
    return {"influenced": [], "influenced_by": [], "papers": papers}


# 爬取aminer网页的数据
def a_get_response(author_id):
    result = {}
    papers = []
    influence = []

    # 加载result，即爬取数据
    url = f'''https://www.aminer.cn/profile/{author_id}'''
    while 1:
        try:
            res = requests.get(url).text
            break
        except requests.exceptions.ConnectionError as e:
            print('error_name:', e.__class__.__name__)
            print('error:', e)
    soup = BeautifulSoup(res, 'lxml')
    data = soup.select('body > script')[0]
    data = re.findall('{\"profile\".*};', str(data))
    res = data[-1][0:-1]
    res = json.loads(res)
    result["name"] = res.get("profile", {}).get("profile", {}).get("name", "")
    result["mechanism"] = res.get("profile", {}).get("profile", {}).get("profile", {}).get("affiliation", "")
    result["title"] = res.get("profile", {}).get("profile", {}).get("profile", {}).get("position", "")
    result["field"] = res.get("profile", {}).get("profile", {}).get("tags", [])
    result["photo"] = res.get("profile", {}).get("profile", {}).get("avatar", "")
    
    # 加载papers，即用于论文匹配的论文列表
    url = 'https://apiv2.aminer.cn/magic'
    url_params = {
        'a': 'GetPersonPubs__person.GetPersonPubs___'
    }
    query = f'''[{{"action": "person.GetPersonPubs","parameters": {{"offset": 0,"size": 10,"sorts": ["!n_citation"],"ids": ["{author_id}"],"searchType": "all"}}, "schema": {{"publication": ["title", "title_zh"]}}}}]'''
    while 1:
        try:
            res = requests.post(url, params=url_params, json=json.loads(query)).json()
            break
        except requests.exceptions.ConnectionError as e:
            print('error_name:', e.__class__.__name__)
            print('error:', e)
    for i in res.get("data")[0].get("items", []):
        papers.append(i.get("title", i.get("title_zh")))
    
    # 加载influence，即与该学者相关的学者id列表
    url = 'https://apiv2.aminer.cn/n'
    url_params = {
        'a': 'GetEgoNetworkGraph__personapi.GetEgoNetworkGraph___'
    }
    query = f'''[{{"action":"personapi.GetEgoNetworkGraph","parameters":{{"id":"{author_id}", "reloadcache":true}}}}]'''
    while 1:
        try:
            res = requests.post(url, params=url_params, json=json.loads(query)).json()
            break
        except requests.exceptions.ConnectionError as e:
            print('error_name:', e.__class__.__name__)
            print('error:', e)
    for i in range(1, len(res.get("data")[0].get("data", []))):
        influence.append(res.get("data")[0].get("data")[i].get("id"))
    
    return result, influence, papers


# 爬取semantic scholar网页的数据
def s_get_response(author_id):
    result = {}
    influenced = []
    influencedBy = []
    papers = []

    # 加载influenced和influencedBy
    url = f'https://www.semanticscholar.org/api/1/author/{author_id}'
    while 1:
        try:
            res = requests.get(url).json()
            break
        except requests.exceptions.ConnectionError as e:
            print('error_name:', e.__class__.__name__)
            print('error:', e)
    for i in res.get("influence", {}).get("influenced", []):
        influenced.append((i.get("author").get("name"), i.get("score", 0)))
    for i in res.get("influence", {}).get("influencedBy", []):
        influencedBy.append((i.get("author").get("name"), i.get("score", 0)))
    
    # 加载papers，即论文列表，限制最多20篇论文
    totalPaperCount = res.get("author", {}).get("statistics", {}).get("totalPaperCount", 0)
    if totalPaperCount>20:
        totalPaperCount = 20
    print("totalPaperCount:", totalPaperCount)
    for i in range(int(totalPaperCount / 10) + 1):
        if i == int(totalPaperCount / 10):
            PaperCount = totalPaperCount % 10
        else:
            PaperCount = 10
        query = f'''{{"queryString":"","page":{i+1},"pageSize":10,"sort":"influence","authors":[],"coAuthors":[],"venues":[],"yearFilter":null,"requireViewablePdf":false,"publicationTypes":[],"externalContentTypes":[],"fieldsOfStudy":[],"useFallbackRankerService":true,"useFallbackSearchCluster":true,"hydrateWithDdb":false,"tldrModelVersion":"v2.0.0","includeTldrs":true}}'''
        while 1:
            try:
                res = requests.post(url, json=json.loads(query)).json()
                break
            except requests.exceptions.ConnectionError as e:
                print('error_name:', e.__class__.__name__)
                print('error:', e)
        for j in range(PaperCount):
            papers.append(res.get("papers").get("results")[j].get("title").get("text"))
    
    result["influenced"] = influenced
    result["influenced_by"] = influencedBy
    result["papers"] = papers
    return result


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # 连接MongoDB
    mydb = myclient["inf_db"]  # 选择数据库
    mycol = mydb["table"]  # 存放爬虫数据的表
    retry = 0
    init = 0  # 是否初始化
    NAME_LIST = []  # 存放待爬取网页id的列表
    if init == 1:  # 初始化操作，清空表，添加种子
        mycol.delete_many({})
        mycol.insert_many([{"_id": "53f43918dabfaee4dc79cbff"}, {"_id": "53f64298dabfaeae621b3a95"}])
    for result in mycol.find({"papers": None}):  # 加载待爬取网页的id
        NAME_LIST.append(result["_id"])
    while len(NAME_LIST) != 0:  # bfs
        try:
            visit = NAME_LIST[0]  # 获取队头网页id
            print("visiting {}".format(visit))
            response, influence, papers = a_get_response(visit)  # 根据id在aminer获取数据
            mycol.update_one({"_id": visit}, {"$set": response})  # 将得到的数据写入MongoDB
            print("aminer data finish")
            response = s_search(response["name"], papers)  # 用学者名称到semantic scholar检索，寻找匹配的页面并爬取数据
            mycol.update_one({"_id": visit}, {"$set": response})  # 将得到的数据写入MongoDB
            print("scholar data finish")
            for id in influence:  # 遍历与该学者有关系的其他学者id
                if mycol.count_documents({"_id": id}) == 0:  # 确认没有被爬取过且没有待爬取
                    mycol.insert_one({"_id": id})  # 标记待爬取
                    NAME_LIST.append(id)  # 将id加入带爬取列表
            NAME_LIST.pop(0)  # 队头弹出
            retry = 0
        except BaseException as e:  # 出现任何错误，输出错误类型
            print('error_name:', e.__class__.__name__)
            print('error:', e)
            traceback.print_exc()
            if e.__class__.__name__ == "IndexError":
                mycol.update_one({"_id": NAME_LIST[0]}, {"$set": {"name": "ErrorPage", "mechanism": "", "title": "", "field": [], "photo": "", "influenced": [], "influenced_by": [], "papers": []}})
                NAME_LIST.pop(0)
            elif e.__class__.__name__ == "KeyboardInterrupt":
                myclient.close()
                sys.exit()
            elif retry == 10:
                myclient.close()
                sys.exit()
            else:
                retry += 1
    myclient.close()
