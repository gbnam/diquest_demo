from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

class rtcIndex(ListView):
    template_name = 'rtc/rtc_index.html'

    def get_queryset(self):
        pass



