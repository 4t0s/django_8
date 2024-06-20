
from django.contrib import admin
from django.urls import path
from app.views import complete_task, show_task, home, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks', show_task, name = 'tasks'),
    path('complete/<int:task_id>', complete_task, name = 'complete'),
    path('delete/<int:task_id>', delete_task, name = 'delete')
]
