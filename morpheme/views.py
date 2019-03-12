import gc
import io
import os
import time

import jpype
import pandas
import psutil
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import MorphemeAnalysisForm
from .models import Morpheme


class MorphemeMainCreateView(LoginRequiredMixin, CreateView):
    template_name = 'morpheme/morpheme_list.html'
    # model = MorphemeAnalysisModel
    form_class = MorphemeAnalysisForm
    # fields = ['raw_sentence', 'slug', 'morpheme_type', 'file']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('morpheme:morpheme_index')

    def form_invalid(self, form):
        return super(MorphemeMainCreateView, self).form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.morpheme_type.id = None
        return super(MorphemeMainCreateView, self).form_valid(form)


# --- Bootstrap Search Result
class SentenceAnalyzeLV(ListView):
    template_name = 'morpheme/morpheme_list.html'

    def get(self, request):
        morpheme_type = '%s' % self.request.GET['morpheme_type']
        sentence = '%s' % self.request.GET['raw_sentence']

        t1 = time.time()
        process = psutil.Process(os.getpid())
        before_mem = process.memory_info().rss / 1024 / 1024

        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                print("before : ", proc)

        morpheme = Morpheme()
        morpheme_object = morpheme.morpheme_init(morpheme_type)
        result_sentence = morpheme_object.pos(sentence)

        after_mem = process.memory_info().rss / 1024 / 1024
        t2 = time.time()
        tot_time = t2 - t1

        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                print("after : ", proc)

        del morpheme
        jpype.java.lang.System.gc()
        gc.collect()

        print('사용 전 메모리 {} MB'.format(before_mem))
        print('실행 후 메모리 {} MB'.format(after_mem))
        print('총 수행 시간 {:.5f}'.format(tot_time))

        context = {}
        context['result_sentence'] = list(result_sentence)
        context['morpheme_type'] = morpheme_type
        context['after_mem'] = after_mem
        context['tot_time'] = tot_time

        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})

    @staticmethod
    def get_data(morpheme_type, result_sentence):
        return {
            'result_sentence': result_sentence
            , 'morpheme_type': morpheme_type
        }


class FileAnalyzeLV(ListView):
    template_name = 'morpheme/morpheme_list.html'

    def post(self, request):
        file_morpheme_type = '%s' % self.request.POST.get('morpheme_type')
        filename = request.FILES['csv_file'].read()

        data_frame = pandas.read_csv(io.BytesIO(filename))
        morpheme_object = Morpheme.morpheme_init(file_morpheme_type)
        morpheme_list = Morpheme.pos_list(morpheme_object, data_frame)
        del morpheme_object
        jpype.java.lang.System.gc()
        return JsonResponse(self.get_data(file_morpheme_type, morpheme_list))

    @staticmethod
    def get_data(file_morpheme_type, morpheme_list):
        return {
            'file_morpheme_type': file_morpheme_type
            , 'morpheme_list': list(morpheme_list)
        }
