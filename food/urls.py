from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    # path('hello/',views.index,name='index')
    path('item/',views.item,name='item'),
    # '' means /food   
]
