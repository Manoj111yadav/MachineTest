from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from taskapp.models import Cleint,User,Project
from taskapp.serializers import CleintSerializer,ProjectSerializer,UserSerializer
from django.core.files.storage import default_storage

@csrf_exempt
def ClientApi(request,id=0):
    if request.method=='GET':
        client = Cleint.objects.all()
        Client_serializer=CleintSerializer(client,many=True)
        return JsonResponse(Client_serializer.data,safe=False)
    elif request.method=='POST':
        Client_data=JSONParser().parse(request)
        Client_serializer=CleintSerializer(data=Client_data)
        if Client_serializer.is_valid():
            Client_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Client_data=JSONParser().parse(request)
        Client=Cleint.objects.get(Client_Id=Client_data["Client_Id"])
        Client_serializer=CleintSerializer(Client,data=Client_data)
        if Client_serializer.is_valid():
            Client_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Client=Cleint.objects.get(Client_Id=id)
        Client.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def UserApi(request,id=0):
    if request.method=='GET':
        Users = User.objects.all()
        User_serializer=UserSerializer(Users,many=True)
        return JsonResponse(User_serializer.data,safe=False)
    elif request.method=='POST':
        User_data=JSONParser().parse(request)
        User_serializer=UserSerializer(data=User_data)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        User_data=JSONParser().parse(request)
        Users=User.objects.get(Id=User_data['Id'])
        User_serializer=UserSerializer(Users,data=User_data)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Users=User.objects.get(Id=id)
        Users.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def ProjectApi(request,id=0):
    if request.method=='GET':
        project = Project.objects.all()
        Project_serializer=ProjectSerializer(project,many=True)
        return JsonResponse(Project_serializer.data,safe=False)
    elif request.method=='POST':
        Project_data=JSONParser().parse(request)
        Project_serializer=ProjectSerializer(data=Project_data)
        if Project_serializer.is_valid():
            Project_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Project_data=JSONParser().parse(request)
        project=Project.objects.get(Project_Id=Project_data['Project_Id'])
        Project_serializer=ProjectSerializer(project,data=Project_data)
        if Project_serializer.is_valid():
            Project_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")