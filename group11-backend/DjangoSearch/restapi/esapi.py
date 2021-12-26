import json
import requests


def resfunc(res):
    resobj = json.loads(res.text)
    reslist = resobj['hits']['hits']
    count = resobj['hits']['total']['value']
    fomatteddata = []

    for obj in reslist:
        fomatteddata.append(obj['_source'])

    result = {
        "value": count,
        "data": fomatteddata
    }

    return result


def search(query, theme, page):
    # theme is name,mechanism,field,paper or empty
    url = "http://localhost:9200/test.data/_search"

    field = [theme]
    if theme == "":
        field = []

    queryobj = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": field
            }
        },
        "from": int(page) * 10,
        "size": 10
    }
    print(queryobj)
    s = json.dumps(queryobj)

    headers = {'Content-type': 'application/json'}
    res = requests.get(url, data=s, headers=headers)
    return resfunc(res)


if __name__ == '__main__':
    print(search())
