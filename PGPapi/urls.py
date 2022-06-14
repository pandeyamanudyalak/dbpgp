from django.urls import path
from . import views

urlpatterns=[
    path('locationapi', views.userLocationAPI.as_view(), name="userLocationAPI"),
    path('locationapi/<int:id>', views.userLocationIDAPI.as_view(), name="userLocationID"),

    path('roleapi', views.userRoleAPI.as_view(),name="userRoleAPI"),
    path('roleapi/<int:id>', views.userRoleIDAPI.as_view(), name="userRoleIDAPI"),

    path('loginapi', views.userLoginAPI.as_view(), name="userLoginAPI"),
    path('loginapi/<int:id>', views.userLoginIDAPI.as_view(), name="userLoginIDAPI"),

    path('userdetailapi', views.userDetailAPI.as_view(), name="userDetailID"),
    path('userdetailapi/<int:id>', views.userDetailIDAPI.as_view(), name="userDetailIDAPI"),

    path('formdataApi', views.formDataAPI.as_view(), name="formDataAPI"),
    path('formdataApi/<int:id>', views.formDataIDAPI.as_view(), name="formDataIDAPI"),

    path('agencyapi', views.agencyNameAPI.as_view(), name="flagAPI"),

    path('filterapi/<str:id>', views.filterSerializer.as_view(),name="filterapi"),
    path('newTask',views.newTask.as_view(),name="newTask"),
    path('newTaskForPerson2',views.newTaskForPerson2.as_view(),name='newTaskForPerson2')
    
]