from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexReport, name="main"),
    path('1', views.firstView, name="first"),
    path('2', views.secondView, name="second"),
    path('3', views.thirdView, name="third"),

]
