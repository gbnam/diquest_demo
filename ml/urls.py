from django.urls import path

from ml import views
from ml.views import MLIndexLV, textrank

app_name = 'ml'
urlpatterns = [
    path('', MLIndexLV.as_view(), name='index'),
    path('textrank/', views.textrank, name='textrank'),
]