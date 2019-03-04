from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Morpheme
from .forms import SentenceForm

"""
1. template에 context를 채워넣어 표현한 결과를 HttpResponse 객체와 함께
돌려주는 구문은 자주 쓰는 용법이나 Django는 이런 표현을 쉽게 표현할 수 있도록
단축 기능(shortcuts)을 제공한다.

def index(request):
    template = loader.get_template('morpheme/morpheme_list.html')
    context = {
        'searchTerm': 'Hello, world. You\'re at the polls index.'
    }
  
    return HttpResponse(template.render(context, request))
"""

"""
2. shortcuts(지름길) 
render() 함수는 request 객체를 첫번째, template 이름을 두번째, context dict 객체를 세번째
선택적 인수로 받는다. 인수로 지정된 context로 표현된 template의 HttpResponse 객체가 반환
"""


class MainFormView(FormView):
    form_class = SentenceForm
    template_name = 'morpheme/morpheme_list.html'

    def form_valid(self, form):
        sentence = '%s' % self.request.POST['raw_sentence']
        context = {}
        context['form'] = form
        context['sentence'] = sentence
        context['result_sentence'] = sentence

        return render(self.request, self.template_name, context)


# --- Bootstrap Search Result
class SentenceAnalyzeLV(ListView):
    template_name = 'morpheme/morpheme_list.html'

    def get(self, request):
        morpheme_type = '%s' % self.request.GET['morpheme_type']
        sentence = '%s' % self.request.GET['raw_sentence']

        morpheme_object = Morpheme.morpheme_init(morpheme_type)
        result_sentence = morpheme_object.pos(sentence)

        return JsonResponse(self.get_data(morpheme_type, result_sentence), json_dumps_params={'ensure_ascii': True})

    @staticmethod
    def get_data(morpheme_type, result_sentence):
        print("XXX")
        return {
            'result_sentence': result_sentence
            , 'morpheme_type': morpheme_type
        }
