from pyexpat import model
from rest_framework import serializers
from .models import Todo,Status

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'        


class StatusSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True,read_only=True)
    class Meta:
        model = Status
        fields = ['id','name','created_at','updated_at','todos']        