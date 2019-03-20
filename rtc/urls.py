from django.urls import path

from rtc.views import rtcIndex

app_name = 'rtc'
urlpatterns = [
    path('', rtcIndex.as_view(), name='index'),
    # path('textrank/', views.textrank, name='textrank'),
]