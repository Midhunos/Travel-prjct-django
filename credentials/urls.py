
from django.urls import path

from . import views

urlpatterns = [

    path('reg',views.Register,name="register"),
    path('log',views.Login,name="log"),
    path('logout',views.Logout,name="logout")

]