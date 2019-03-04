from django.urls import path

from ml.views import MLIndexLV

app_name = 'ml'
urlpatterns = [
    path('', MLIndexLV.as_view(), name='index'),
]