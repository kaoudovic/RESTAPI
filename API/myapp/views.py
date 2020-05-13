from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from .json import json_student
from rest_framework.views import APIView
from .models import student
from rest_framework import viewsets


############################
# first way API
########3
class student_list(APIView):
    def get(self, request):
        s1 = student.objects.all()  # all data
        s2 = json_student(s1, many=True)
        return Response(s2.data)

    def post(self):
        pass


##################################

# second way API
class student_list1(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = json_student

##################################

def index(request):
    return render(request, 'index.html', {})
