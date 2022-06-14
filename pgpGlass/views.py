from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from . import API
import pgpGlass
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_area(request):
    response = requests.get(API.LOCATION_GET_POST)
    data = response.json()
    if request.method=="POST":
        get_loction = request.POST.get('city')
        userDetails=requests.get(API.USER_ROLE+ str(get_loction))
        userDetailsjson=userDetails.json()
        print(userDetailsjson)
        
        return render(request, 'pgpGlass/select_role.html',{'data':userDetailsjson})

    return render(request,'pgpGlass/location.html',{'all_area':data})

def get_filtered_name(request):
    if request.method == "POST":
        ddl1 = request.POST['ddl1']
        print("DDL1************", ddl1)
        ddl2 = request.POST['ddl2']
        print("DDL2************", ddl2)
        ddl3 = request.POST['ddl3']
        print("DDL3************", ddl3)
        return render(request,'pgpGlass/add_new_task.html')
    return render(request, 'pgpGlass/select_role.html')

def addTask(request):
    return render(request, 'pgpGlass/add_new_task.html')

def newTask(request):
    data=requests.get(API.NEW_TASKS)
    form_data_json=data.json()
    print(data)
    return render(request,'pgpGlass/new_task.html',{'data':form_data_json})

# @csrf_exempt
# def approvedByPerson1(request):
#     if request.method== 'POST':
#         name=request.POST['loggedPerson']
#         print(name)
#         data=requests.put(API.FORM_GET_PUT_DELETE_ID)
#         return redirect('/')


def newTaskForPerson2(request):
    data=requests.get(API.NEW_TASK_PERSON_2)
    data_json=data.json()
    return render(request,'pgpGlass/new_task_person.html',{'data':data_json})
 

@csrf_exempt
def approvedByPerson1(request,id):
    data={'verifiyedByPerson1Flag':True}
    update_data=requests.post(API.FORM_GET_PUT_DELETE_ID+str(id),data=data)
    return HttpResponse(update_data)