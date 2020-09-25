from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('checkout/',views.checkout,name="checkout"),
    path('trial/',views.trial,name="trial"),
    path('qv/<int:myid>',views.qv,name="qv"),
    path('rate/<int:myid>',views.rate,name="rate"),
    path('handlerequest/',views.handlerequest,name="handlerequest"),

]