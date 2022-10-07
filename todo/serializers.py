from pyexpat import model
from rest_framework import serializers
from .models import Todo,Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'        


class TodoSerializer(serializers.ModelSerializer):
    todos = StatusSerializer(many=True,read_only=True)
    class Meta:
        model = Todo
        fields = ['id','name','created_at','updated_at','todos']        