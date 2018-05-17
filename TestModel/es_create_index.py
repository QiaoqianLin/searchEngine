# coding: utf-8

# 创建 jianshu 索引，指定 document 类型

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'localhost', 'port': 9200}])

body = {
    "mappings" : {
        "ariticle" : {
            "properties" : {
                "url" : {                 # url 
                    "type" : "text"
                },
                # "title" : {               # 标题
                #     "type" : "text",
                #     "analyzer": "english",
                #     "search_analyzer": "english"
                # },
                "content" : {             # 正文
                    "type" : "text",
                    "analyzer": "english",
                    "search_analyzer": "english"
                }
            }
        }
    }
}

es.indices.create(index='cs_index', body=body)

