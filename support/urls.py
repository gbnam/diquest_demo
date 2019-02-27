from django.urls import path

from .views import *

app_name = 'support'
urlpatterns = [

    # Example: /
    path('', SupportLV.as_view(), name='index'),

    # Example: /support/viewer/1
    path('support/pdf_viewer/<int:pk>', SupportPV.as_view(), name='support_pdf_viewer'),

    # Example: /support/ (same as /)
    path('support/', SupportLV.as_view(), name='support_list'),

    # Example: /support/django-example/
    path('support/<slug>/', SupportDV.as_view(), name='support_detail'),

    # Example: /tag/
    path('tag/', TagTV.as_view(), name='tag_cloud'),

    # Example: /tag/tagname/
    path('tag/<str:tag>/', SupportTOL.as_view(), name='tagged_object_list'),

    # Example: /search/
    path('search/', SearchFormView.as_view(), name='search'),

    # Example: /bssearch/ (Bootstrap Search)
    path('bssearch/', BstrapSearchLV.as_view(), name='bssearch'),

    # Example: /add/
    path('add/',
         SupportCreateView.as_view(), name="add",
         ),

    # Example: /change/
    path('change/',
         SupportChangeLV.as_view(), name="change",
         ),

    # Example: /99/update/
    path('<int:pk>/update/',
         SupportUpdateView.as_view(), name="update",
         ),

    # Example: /99/delete/
    path('<int:pk>/delete/',
         SupportDeleteView.as_view(), name="delete",
         ),
]
