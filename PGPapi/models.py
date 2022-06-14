from django.db import models
from datetime import date, time

# Create your models here.
class userLogin(models.Model):
   name = models.CharField(max_length=200, blank=True, null=True)
   email = models.EmailField(max_length=200, blank=True, null=True)
   password = models.CharField(max_length=200)
   def __str__(self):
      return self.name

class userLocation(models.Model):
   location = models.CharField(max_length=200, blank=True, null=True)
   def __str__(self):
      return self.location

class userRole(models.Model):
   roleName = models.CharField(max_length=200, blank=True, null=True)
   def __str__(self):
      return self.roleName

class userDetails(models.Model):
   userName = models.ForeignKey(userLogin, on_delete=models.CASCADE, blank=True, null=True)
   userLocation = models.ForeignKey(userLocation, on_delete=models.CASCADE, blank=True, null=True)
   userRole = models.ForeignKey(userRole, on_delete=models.CASCADE, blank=True, null=True)
   def __str__(self):
      #return str(self.userName)
      return u" %s %s %s "%(self.userName,self.userLocation,self.userRole)

class issueAgency(models.Model):
   agencyName = models.CharField(max_length=200, blank=True, null=True)
   def __str__(self):
      return str(self.agencyName)

class formData(models.Model):
   loggedPerson = models.ForeignKey(userLogin, on_delete=models.CASCADE)
   date = models.DateField()
   typeOfWork=models.CharField(max_length=500,blank=True, null=True)
   numberOfPerson = models.IntegerField()
   startTime = models.TimeField()
   endTime= models.TimeField()
   location = models.ForeignKey(userLocation, on_delete=models.CASCADE)
   equipment = models.CharField(max_length=200, blank=True, null=True)
   toolRequired = models.CharField(max_length=200, blank=True, null=True)
   workingAgency=models.ForeignKey(issueAgency, on_delete=models.CASCADE)
   workDescription = models.CharField(max_length=500, blank=True, null=True)
   ppeRequired = models.CharField(max_length=200, blank=True, null=True)
   person1 = models.ForeignKey(userLogin, related_name="person1", on_delete=models.CASCADE)
   person2 = models.ForeignKey(userLogin, related_name="person2", on_delete=models.CASCADE)
   verifiyedByPerson1Flag =models.BooleanField(default=False,null=True)
   newFlag = models.BooleanField(default=False,null=True)
   oldFlag = models.BooleanField(default=False,null=True)
   closeFlag = models.BooleanField(default=False,null=True)
   completedFlag = models.BooleanField(default=False,null=True)
   
   def __str__(self):
      #return str(self.pk)
      return u" %s %s %s %s %s %s %s %s %s %s "%(self.loggedPerson,self.date,self.typeOfWork,self.numberOfPerson,self.startTime,self.endTime,self.endTime,self.location,self.equipment,self.toolRequired)


class person(models.Model):
   person = models.ForeignKey(userLogin, on_delete=models.CASCADE)
   form = models.ForeignKey(formData, on_delete=models.CASCADE)
   new_notification = models.BooleanField(default=False)


