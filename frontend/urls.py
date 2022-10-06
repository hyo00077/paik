from django.urls import path, include
from .views import input_main
from django.conf import settings


urlpatterns = [
    path("report", input_main, name="main"),
    path("report/<int:report>", input_main, name="report"),
    path("sentence/<int:report>/share", input_main),
]
