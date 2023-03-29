from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('Task/Add', views.ADD_TASK, name='add_task'),
    path('Task/Save', views.SAVE_TASK, name='save_task'),
    path('Task/Delete/<str:task_id>', views.DELETE_TASK, name='delete_task')
]
