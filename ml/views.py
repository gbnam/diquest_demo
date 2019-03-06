import json

from django.http import HttpResponse
from django.views.generic import ListView

from ml.textRank import TextRank


class MLIndexLV(ListView):
    template_name = 'ml/ml_list.html'

    def get_queryset(self):
        pass


def textrank(request):
    print("textrank views.py")
    # sentence = ['안녕하세요', '저는 김호근입니다', '반갑습니다']
    # keyword = ['안녕', '저는', '김호근']
    context = request.POST['originalText']
    tr = TextRank(context)
    sentence = tr.summarize()
    keyword = tr.summaryKeyword()
    print("원문: {}".format(context))
    print("요약 문장: {}".format(sentence))
    print("요약 키워드: {}".format(keyword))

    result = {
        'sentence': sentence,
        'keyword': keyword,
    }
    print("result: ", result)
    return HttpResponse(json.dumps(result), 'application/json')
