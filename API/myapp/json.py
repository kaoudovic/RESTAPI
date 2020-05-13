from .models import student
from rest_framework import serializers


class json_student(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'  #  =  ['id','fname','lname','age','degree','department']
