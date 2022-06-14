from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.

############# GET and POST REQUEST of userLocation MODEL ##############
class userLocationAPI(APIView):
    def get(self, request, *args,**kwargs):
        user_location= userLocation.objects.all()
        get_userlocation_data = userLocationSerializer(user_location, many=True)
        return JsonResponse(get_userlocation_data.data, safe=False)

    def post(self, request, *args,**kwargs):
        serializer=userLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'})
        return JsonResponse(serializer.errors)

############# GET, UPDATE, DELETE from ID of userLocation MODEL ##############
class userLocationIDAPI(APIView):
    def get_object(self, id):
        try:
            return userLocation.objects.get(pk=id)
        except userLocation.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        locationobj = self.get_object(id)
        serializer = userLocationSerializer(locationobj)
        return JsonResponse(serializer.data)

    def put(self, request, id,*args,**kwargs):
        user_location= self.get_object(id)
        serializer = userLocationSerializer(user_location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of userRole MODEL ##############
class userRoleAPI(APIView):
    def get(self, request, *args,**kwargs):
        user_role= userRole.objects.all()
        get_userRole_data = userRoleSerializer(user_role, many=True)
        return JsonResponse(get_userRole_data.data, safe=False)

    def post(self, request, *args,**kwargs):
        serializer=userRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'})
        return JsonResponse(serializer.errors)

############# GET, UPDATE, DELETE from ID of userRole MODEL ##############
class userRoleIDAPI(APIView):
    def get_object(self, id):
        try:
            return userRole.objects.get(pk=id)
        except userLocation.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        roleobj = self.get_object(id)
        serializer = userRoleSerializer(roleobj)
        return JsonResponse(serializer.data)

    def put(self, request, id,*args,**kwargs):
        userRole= self.get_object(id)
        serializer = userRoleSerializer(userRole, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of userDetails MODEL ##############
class userLoginAPI(APIView):
    def get(self, request, *args,**kwargs):
        user_login= userLogin.objects.all()
        get_userdetail_data = userLoginSerializer(user_login, many=True)
        return JsonResponse(get_userdetail_data.data, safe=False)

    def post(self, request, *args,**kwargs):
        serializer=userLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'})
        return JsonResponse(serializer.errors)

############# GET, UPDATE, DELETE from ID of userDetails MODEL ##############
class userLoginIDAPI(APIView):
    def get_object(self, id):
        try:
            return userLogin.objects.get(pk=id)
        except userLogin.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = userLoginSerializer(getobj)
        return JsonResponse(serializer.data)

    def put(self, request, id,*args,**kwargs):
        userLogin= self.get_object(id)
        serializer = userLoginSerializer(userLogin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of userDetails MODEL ##############
class userDetailAPI(APIView):
    def get(self, request, *args,**kwargs):
        user_detail= userDetails.objects.all()
        get_userdetail_data = userDetailSerializer(user_detail, many=True)
        return JsonResponse(get_userdetail_data.data, safe=False)

    def post(self, request, *args,**kwargs):
        serializer=userDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'})
        return JsonResponse(serializer.errors)

############# GET, UPDATE, DELETE from ID of userDetails MODEL ##############
class userDetailIDAPI(APIView):
    def get_object(self, id):
        try:
            return userDetails.objects.get(pk=id)
        except userDetails.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = userDetailSerializer(getobj)
        return JsonResponse(serializer.data)

    def put(self, request, id,*args,**kwargs):
        userDetail= self.get_object(id)
        serializer = userDetailSerializer(userDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of Form MODEL ##############
class formDataAPI(APIView):
    def get(self, request, *args,**kwargs):
        form_data= formData.objects.all()
        get_from_data = formDataSerializer(form_data, many=True)
        return JsonResponse(get_from_data.data, safe=False)

    def post(self, request):
        serializer = formDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'})
        return JsonResponse(serializer.errors)

############# GET, UPDATE, DELETE from ID of FORM MODEL ##############
class formDataIDAPI(APIView):
    def get_object(self, id):
        try:
            return formData.objects.get(pk=id)
        except formData.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = formDataSerializer(getobj)
        return JsonResponse(serializer.data)

    def post(self, request, id,*args,**kwargs):
        formDetail= self.get_object(id)
        serializer = formDataSerializer(formDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of FLAG MODEL ##############
class agencyNameAPI(APIView):
    def get(self, request, *args,**kwargs):
        agency_data= issueAgency.objects.all()
        get_agency_data = issueAgencySerializer(agency_data, many=True)
        return JsonResponse(get_agency_data.data, safe=False)

    def post(self, request):
        serializer = issueAgencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'})
        return JsonResponse(serializer.errors)

############# GET, UPDATE, DELETE from ID of FLAG MODEL ##############

class issueAgencySerializer(APIView):
    def get_object(self, id):
        try:
            return issueAgency.objects.get(pk=id)
        except issueAgency.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = issueAgencySerializer(getobj)
        return JsonResponse(serializer.data)

    def put(self, request, id,*args,**kwargs):
        issueAgencyDetail= self.get_object(id)
        serializer = issueAgencySerializer(issueAgencyDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# FILTER DATA ACCORDING TO THE LOCATION SELECTED ##############
class filterSerializer(APIView):
    def get(self, request, id, *args, **kwargs):
        user_details = userDetails.objects.filter(userLocation=id)
        user_detail = userDetailSerializer(user_details, many=True)
        print(user_details)
        return JsonResponse(user_detail.data, safe=False)


class newTask(APIView):
    def get(self,request):
        new_data=formData.objects.all().filter(person1=4)
        serialized_data=formDataSerializer(new_data,many=True)
        return JsonResponse(serialized_data.data,safe=False)


class newTaskForPerson2(APIView):
    def get(self,request):
        new_task_data=formData.objects.filter(verifiyedByPerson1Flag=True,person2=2)
        serialized_data=formDataSerializer(new_task_data,many=True)
        return JsonResponse(serialized_data.data,safe=False)


