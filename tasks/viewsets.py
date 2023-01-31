from rest_framework import viewsets

from .models import Todo
from .serializers import TaskSerializer

class MissingTaskViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(done = False)
    serializer_class = TaskSerializer