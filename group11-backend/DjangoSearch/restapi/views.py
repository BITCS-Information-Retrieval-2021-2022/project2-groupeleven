from django.shortcuts import render
from django.http import HttpResponse

from . import esapi
import json
# Create your views here.


def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# 搜索接口
# 请求地址 localhost:8000/search?query=北京&theme=institution&page=1
# 请求方法 Get
# 参数 搜索关键字 query(string) 必填
# 搜索字段 theme(string) 必选 取值：empty,name,institution,field,paper
# 页面 page(String) 必选 代表返回的页数,从0开始


def search(request):
    request.encoding = 'utf-8'
    query = request.GET['query']
    # print("OK")
    if 'theme' in request.GET and request.GET['theme']:
        theme = request.GET['theme']
    else:
        theme = ""
    if 'page' in request.GET and request.GET['page']:
        page = request.GET['page']
    else:
        page = None

    if theme == "institution":
        theme = "mechanism"

    result = esapi.search(query, theme, page)
    # result = esapi.search()
    return HttpResponse(json.dumps(result))
