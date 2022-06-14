from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(userRole)
class userRoleAdmin(admin.ModelAdmin):
    list_display = ['id','roleName']

@admin.register(userLogin)
class userLoginAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']

@admin.register(userLocation)
class userLocationAdmin(admin.ModelAdmin):
    list_display = ['id','location']

@admin.register(userDetails)
class userDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','userName','userLocation','userRole']

@admin.register(issueAgency)
class issueAgencyAdmin(admin.ModelAdmin):
    list_display = ['id','agencyName']

@admin.register(formData)
class formDataAdmin(admin.ModelAdmin):
    list_display = ['id','loggedPerson','date','typeOfWork','numberOfPerson','startTime','endTime','location',
                    'equipment','toolRequired','workingAgency','workDescription','ppeRequired','person1','person2',
                    'newFlag', 'oldFlag', 'closeFlag', 'completedFlag'
                    ]

@admin.register(person)
class personAdmin(admin.ModelAdmin):
    list_display = ['id','person','form','new_notification']