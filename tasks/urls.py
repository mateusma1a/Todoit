from django.urls import path, include
from . import views
from .routers import router

urlpatterns = [
    path('', views.show_tasks),
    path('new/', views.new_task),
    path('edit/<int:task_id>', views.edit_task),
    path('delete/<int:task_id>', views.delete_task),
    path('api/', include(router.urls)),
]