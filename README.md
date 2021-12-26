# groupEleven
## 基于Vue + Element-UI + Django + Elastic Search的学者检索项目

# 目录

- [项目启动流程](##环境要求)
  - [环境要求](#环境要求)
  - [部署过程](#部署过程)
  - [运行项目](#运行项目)
- [前端目录结构](#前端目录结构)
- [后端目录结构](#后端目录结构)
- [项目功能展示](#项目功能展示) 
- [前后端接口说明](#前后端接口说明)
- [前端页面之间参数传递](#前端页面之间参数传递)
- [第三方库依赖](#第三方库依赖)
- [小组分工](#小组分工)

##  项目启动流程

### 环境要求

- NodeJS 8.12+ 
- python 3.0+

###  部署过程

1. 前端

```bash
前端 Vue + ElementUI
#1. 需要安装node.js （本项目node.js版本号为10.20.1）
#2. 安装Vue所需的依赖
cd 到文件目录 
npm install
#3. 启动前端项目
npm run dev
```

2. 后端

```bash
后端 Django + Elastic Search
# 1. 需要安装Python环境 （本项目Python版本为3.8.12）
# 2. 安装Django
sudo pip3 install Django
# 3. cd到后端项目文件目录下
cd DjangoSearch
# 4. 启动Django服务
python manage.py runserver
# 5. 安装Elastic Search环境（本项目版本为7.16.2）
# 6. 解压文件后运行 /bin文件下elasticsearch.bat
cd elasticsearch-7.16.2/bin/
elasticsearch.bat
```

### 运行项目

~~~shell
$ npm run dev # 开发环境下运行Vue
$ python manage.py runserve # 启动 Django
$ elasticsearch.bat # 启动 Elastic Search
~~~

## 前端目录结构

~~~bash
├─ static
|  ├─ images 		        // 存放图片（学者搜索引擎logo、背景图、搜索页面学者默认头像、学者详情页头像框）
├─ src
│  ├─ components  	        // 存放所有组件 component
│  │  ├─ CopyRight.vue  	// 版权信息组件
│  │  ├─ Index.vue 	        // 首页
│  │  ├─ LocalHeader.vue  	// 首页头部组件
│  │  ├─ Profile.vue  	    // 学者详情页
│  │  ├─ SearchPage.vue  	// 检索结果页
│  │  ├─ SearchWindows.vue  // 检索组件
│  ├─ router      	        // vue路由的配置文件
│  ├─ store 
│  │  ├─ index.js           // 应用级数据（state）
│  ├─ App.vue   	        // 根组件
│  └─ main.js   	        // 入口js文件
~~~

## 后端目录结构

~~~bash
├─ DjangoSearch
│   ├─ DjangoSearch
│   │  ├─  asgi.py
│   │  ├─  settings.py		// 项目配置
│   │  ├─  urls.py			// 项目路由设置
│   │  ├─  wsgi.py			// nginx/apache
│   │  ├─  __init__.py
│   ├─ restapi				// 应用
│   │   ├─  admin.py
│   │   ├─  apps.py
│   │   ├─  esapi.py		// 调用Elastic Search的接口
│   │   ├─  models.py
│   │   ├─  tests.py
│   │   ├─  urls.py			// 路由设置
│   │   ├─  views.py		// 控制层
│   │   ├─  __init__.py
│   │   ├─ migrations
│   │   │  │  __init__.py
│   ├─ db.sqlite3
│   └─ manage.py
~~~

## 项目功能展示

系统总共由三个部分组成，分别为1.首页 2.检索结果页 3.学者详情页

### 首页

a)	可按照姓名、机构、领域、论文字段指定一个进行搜索

b)	不指定检索自段则默认全文检索

c)	检查输入是否合法

![](D:\xinxijiansuo\website-helloworld-master\shouye.PNG)

### 检索结果页

a)	显示检索所用时间

b)	内容主体显示每一条记录的学者姓名、职称、研究机构和研究领域

c)	按照相关度进行结果排序

d)   点击导航条上的网站名可以返回首页

e)   点击学者姓名可以进入学者详情页



### 学者详情页

a)	显示学者姓名、头像、职称、研究机构、研究领域和文章列表

b)	为每位学者添加头像框

c)	页面下方显示人物关系图网，利用 Echarts 做具体展示



## 前后端接口说明

### 1.搜索接口

| 接口详情 |                        |
| -------- | ---------------------- |
| 地址     | localhost:8000/search/ |
| 请求方式 | `GET`                  |

#### url示例

localhost:8000/search/?query=wei&theme=name&page=0

## 前端页面之间参数传递

~~~bash
1、搜索页跳转到检索结果列表页
query:{
    theme: “” or “paper” or “name” or “institution” or “field” ,   // 检索方式 
    keyword: “”  // 输入文本框中的内容 
}
2、检索结果列表页跳转到作者profile页面
query:{
	Infors:{
		name:””,          //学者姓名
		photo:””,         //学者头像
		title:””,         //学者职称
		mechanism:””,     //学者工作机构
		field:[],         //学者研究领域
		papers:[],        //学者的论文
		influenced:[],    //学者对其他学者的影响
		influenced by:[]  //学者受其他学者的影响
	}
}

~~~



## 爬虫和数据库

### 1.数据库字段含义

name		姓名		字符串

photo		照片地址		字符串

title		职称		字符串

mechanism	所属机构		字符串

papers		论文名称列表	字符串列表

field		研究领域		字符串列表

influenced	影响了该学者的人名	[{"name": 字符串, "value": 整数}, {}, ...]

influenced_by	被该学者影响的人名	[{"name": 字符串, "value": 整数}, {}, ...]

### 2.字段覆盖率

数据总条数：16693

aminer数据条数：16693

scholar数据条数：9189

name		姓名		99.98%

photo		照片地址		20.89%

title		职称		21.69%

mechanism	所属机构		69.19%

papers		论文名称列表	82.00%

field		研究领域		77.82%

influenced	影响了该学者的人名	55.05%

influenced_by	被该学者影响的人名	55.03%



## 第三方库依赖

|                        依赖库                        |                             版本                             |                             文档                             |                     介绍                     |
| :--------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :------------------------------------------: |
|       [axios](https://github.com/axios/axios)        | [![npm version](https://img.shields.io/badge/npm-v0.18.0-orange)](https://www.npmjs.org/package/axios) |     [axios docs(zh-CN)](http://axios-js.com/zh-cn/docs/)     |           基于 promise 的 HTTP 库            |
| [vue-axios](https://github.com/imcvampire/vue-axios) | [![npm version](https://img.shields.io/badge/npm-v2.1.4-orange)](https://www.npmjs.com/package/vue-axios) | [vue-axios docs(zh-CN)](http://www.axios-js.com/zh-cn/docs/vue-axios.html) |       基于 Vue.js 和 axois 的轻度封装        |
| [element-ui](https://github.com/ElemeFE/element.git) | [![npm version](https://img.shields.io/badge/npm-v2.7.2-orange)](https://www.npmjs.com/package/element-ui) | [element-ui docs(zh-CN)](https://element.eleme.cn/#/zh-CN/component/installation) |        基于 Vue 2.0 开发的开源组件库         |
|  [vue-router](https://github.com/vuejs/vue-router)   | [![npm version](https://img.shields.io/badge/npm-v3.0.1-orange)](https://www.npmjs.com/package/vue-router) | [vue-router docs(zh-CN)](https://router.vuejs.org/zh/installation.html) |             Vue 官方的路由管理器             |
|        [vuex](https://github.com/vuejs/vuex)         | [![npm version](https://img.shields.io/badge/npm-v3.1.0-orange)]() |        [vuex docs(zh-CN)](https://vuex.vuejs.org/zh/)        | 专为 Vue.js 应用程序开发的**状态管理模式**库 |
|   [monstache](https://github.com/rwynn/monstache)    | [![Monstache CI](https://github.com/rwynn/monstache/workflows/Monstache%20CI/badge.svg?branch=rel6)](https://github.com/rwynn/monstache/actions?query=branch%3Arel6) | [monstache docs(en-US)](https://rwynn.github.io/monstache-site/) | 用于同步MongoDB服务器与Elastic Search的数据  |
|       [requests](https://github.com/psf/requests)        | 2.24.0 | [requests docs(en-US)](https://docs.python-requests.org/en/latest/)         |           python实现的简单易用的HTTP库            |

## 小组分工 

|   姓名   |    学号    |       分工        | 职务 |
| :------: | :--------: | :---------------: | :--: |
|  陈轶飞  | 3220211147 | 后端+后端页面接口 | 组员 |
|  朱宇博  | 3120211052 | 爬虫+数据库       | 组员 |
|  李晓雨  | 3220211169 | 爬虫+数据库       | 组员 |
|  毕蓓    | 3120211030 | 前端+前端页面接口 | 组员 |
|  高思睿  | 3220211003 | 前端             | 组员 |
|  李逸文  | 3120211038 |       后端        | 组长 |





































































