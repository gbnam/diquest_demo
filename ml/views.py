import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class MLIndexLV(ListView):
    template_name = 'ml/ml_list.html'

    def get_queryset(self):
        pass

def textrank(request):
    print("textrank views.py: {}".format(request.POST['originalText']))

    sentence = ['안녕하세요', '저는 김호근입니다', '반갑습니다']
    keyword = ['안녕', '저는', '김호근']
    print(sentence, keyword)
    result = {
        'sentence' : sentence,
        'keyword' : keyword,
    }
    return HttpResponse(json.dumps(result), 'application/json')
