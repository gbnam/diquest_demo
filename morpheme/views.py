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
from .models import MorphemeAnalysisModel, Morpheme


def decorator_function(get):
    def wrapper_function(*args):
        return get(*args)

    return wrapper_function


def process_check():
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss / 1024 / 1024

    for proc in psutil.process_iter():
        if proc.name() == "python.exe":
            print(proc)
    return memory


class MorphemeMainCreateView(LoginRequiredMixin, CreateView):
    template_name = 'morpheme/morpheme_list.html'
    form_class = MorphemeAnalysisForm
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('morpheme:morpheme_index')


class SentenceAnalyzeLV(ListView):
    template_name = 'morpheme/morpheme_list.html'

    def post(self, request):
        morpheme_type = '%s' % self.request.POST.get('morpheme_type')
        sentence = '%s' % self.request.POST.get('raw_sentence')
        user_name = '{0}'.format(self.request.user)

        start_time = time.time()
        before_memory = process_check()

        morpheme = Morpheme()
        morpheme_object = morpheme.morpheme_init(morpheme_type)
        result_sentence = morpheme_object.pos(sentence)

        after_memory = process_check()
        end_time = time.time()
        total_time = end_time - start_time
        total_memory = after_memory - before_memory

        del morpheme
        jpype.java.lang.System.gc()
        gc.collect()

        context = {}
        context['result_sentence'] = list(result_sentence)
        context['morpheme_type'] = morpheme_type
        context['total_memory'] = float('{:.3f}'.format(total_memory))
        context['user_name'] = ''.join(char for char in user_name if char not in '"')
        context['total_time'] = float('{:.3f}'.format(total_time))

        model = MorphemeAnalysisModel(raw_sentence=sentence, morpheme_type=morpheme_type)
        model.save()

        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})


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
        model = MorphemeAnalysisModel(raw_sentence=filename, morpheme_type=file_morpheme_type, file=request.FILES['csv_file'])
        model.save()

        return JsonResponse(self.get_data(file_morpheme_type, morpheme_list))

    @staticmethod
    def get_data(file_morpheme_type, morpheme_list):
        return {
            'file_morpheme_type': file_morpheme_type
            , 'morpheme_list': list(morpheme_list)
        }
