from django.urls import path

from .views import *

""" app_name이 꼭 있어야 core/urls.py에서 인식함 """
app_name = 'morpheme'

urlpatterns = [
    # ex : /morpheme/, parameter : context path, view name, view role
    path('', MainFormView.as_view(), name='index'),

    path('sentence/', SentenceAnalyzeLV.as_view(), name='get'),

    path('morpheme_file/', FileAnalyzeLV.as_view(), name='file_add'),
]
