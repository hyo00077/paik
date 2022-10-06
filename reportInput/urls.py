from django.urls import path
from . import views

urlpatterns = [
    path('report/all', views.ReportList.as_view(), name="reportList"),
    path('report/<int:report>', views.ReportStringList, name="eachyReport"),
    path('report/<int:report>/<int:pk>',
         views.getSentence, name="getSentence"),
    path('sentence/<int:sentence>', views.shareSentence, name="shareSentence")
]
