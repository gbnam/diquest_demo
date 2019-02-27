from django.urls import path

from .views import *



app_name = 'product'
urlpatterns = [
    path('', ProductLV.as_view(), name='index'),
    path('<int:pk>/', ProductDV.as_view(), name='detail'),

    # Example: /add/
    path('add/',
         ProductCreateView.as_view(), name="add",
    ),

    # Example: /change/
    path('change/',
         ProductChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    path('<int:pk>/update/',
         ProductUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    path('<int:pk>/delete/',
         ProductDeleteView.as_view(), name="delete",
    ),
]
