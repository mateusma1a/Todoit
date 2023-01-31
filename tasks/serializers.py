from rest_framework import serializers
from .models import Todo

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'text', 'done')