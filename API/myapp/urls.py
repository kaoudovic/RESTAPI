from django.urls import path,include
from .views import index,student_list
from rest_framework import routers
r=routers.DefaultRouter()
r.register('',student_list)
urlpatterns = [
    path('',index,name='index'),
    path('student_json',student_list.as_view()),
    path('student_json1',include(r.urls)),

]