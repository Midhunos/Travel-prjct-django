
from django.urls import path

from . import views

urlpatterns = [

    path('',views.demo,name="demo"),
    path('abot/',views.about,name="abt"),
    # path('add/',views.addition,name="addd")
]