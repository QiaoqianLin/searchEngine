from django.shortcuts import render
from .models import Contact
from .forms import AddForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .index_data import index_data
import json

from django.views.decorators import csrf
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200}])
# Create your views here.
# def remark(request):
#     if request.method == 'POST':  # 如果表单被提交
#         form = ContactForm(request.POST)  # 获取Post表单数据
#         # if form.is_valid():  # 验证表单
#         #     return HttpResponseRedirect('/')  # 跳转
#     else:
#         form = ContactForm()  # 获得表单对象
#
#     return render(request,'message.html', {
#         'form': form,
#     })

#
# def index(request):
#     ctx = {}
#     if request.method == 'POST':  # 当提交表单时
#
#         form = AddForm(request.POST)  # form 包含提交的数据
#
#         if form.is_valid():  # 如果提交的数据合法
#             ctx['rlt'] = form.cleaned_data['contact_name']
#             b = form.cleaned_data['contact_group']
#             # return HttpResponse(str(a) + str(b))
#
#     else:  # 当正常访问时
#         form = AddForm()
#     return render(request, 'message.html', {'form': form})

def index(request):
    ctx = {}
    res = {}
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            ctx['rlt'] = form.cleaned_data['keywords']
            group = form.cleaned_data['type']
            index_data(group)

            result = es.search(index='cs_index', doc_type='ariticle', body={
                "query": {"match": {"content": ctx['rlt']}},
                "from": 0,
                "size": 5
            })
            i = 0
            for item in result['hits']['hits']:
                res[i] = 'url:   ' + item['_source']['url'] + 'score: ' + str(item['_score'])
                i += 1
            return HttpResponse(json.dumps(res))
    #
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'message.html', {'form': form})
    # return render(request, "message.html", {"dicts":res})


def start(request):
    # context          = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'a.html')

