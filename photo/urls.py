from django.urls import path

from .views import *


app_name = 'photo'

urlpatterns = [

    # Example: /
    path('', PhotoLV.as_view(), name='index'),

    # Example: /photo/99/
    path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),


    # Example: /photo/add/
    path('photo/add/',
         PhotoCreateView.as_view(), name="photo_add",
    ),

    # Example: /photo/change/
    path('photo/change/',
         PhotoChangeLV.as_view(), name="photo_change",
         ),

    # Example: /photo/99/update/
    path('photo/<int:pk>/update/',
         PhotoUpdateView.as_view(), name="photo_update",
    ),

    # Example: /photo/99/delete/
    path('photo/<int:pk>/delete/',
         PhotoDeleteView.as_view(), name="photo_delete",
    ),
]

