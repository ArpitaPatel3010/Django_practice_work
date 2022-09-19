from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("forms/",form_page),
    path("submit/",form_submit),
    path("data_page/",data_page),
    path("get_data/",get_data),
    path("update_page/",update_page),
]