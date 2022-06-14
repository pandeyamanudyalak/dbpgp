from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_area, name="area"),
    path('select_role',views.get_filtered_name, name="select_role"),
    path('addTask',views.addTask, name="addtask"),
    path('newTask',views.newTask, name="newtask"),
    path('approvedByPerson1/<str:id>',views.approvedByPerson1,name="approvedByPerson1"),
    path('newTaskForPerson2',views.newTaskForPerson2,name="newTaskForPerson2")

]