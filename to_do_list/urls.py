from django.urls import path
from to_do_list import views

urlpatterns = [
    path('',views.index,name='home'),
    path('',views.remove,name='remove')
]