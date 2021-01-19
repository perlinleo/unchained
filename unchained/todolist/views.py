from django.shortcuts import render

from todolist import models
from todolist import serializers
from todolist import forms
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Task.objects.filter()
    serializer_class = serializers.TaskSerializer

class ToDoListViewSet(viewsets.ModelViewSet):
    account = models.Account()
    def getId(self):
        account = (models.Account.objects.get(UserLink=self.request.user.pk))
        id1 = account.id
        return id1
    def __str__(self,*args,**kwargs):
        account = (models.Account.objects.get(UserLink=self.request.user.pk))
        return "privet hailadji"
    def get_queryset(self):
        print(self)
        account = (models.Account.objects.get(UserLink=self.request.user.pk))
        id1 = account.id
        return models.ToDoList.objects.filter(AccountLink=id1)
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.ToDoList.objects.filter()
    
    serializer_class = serializers.ToDoListSerializer

class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer




@api_view(http_method_names=['POST'])
def clown(request):
    print(request.body)
    data = json.loads(request.body.decode())
    print(data)
    if(not data["Change"]==False):
        print(data["Change"])
        print(data["ChangeID"])
        task = models.Task.objects.get(id=data["ChangeID"])
        task.Finished = not task.Finished
        task.save()
    else:
        Finished =data["Finished"]
        finishedsave = Finished=='true'
        print (data["Finished"])
        print (finishedsave)
        task = models.Task(Description=data["Description"],Label=data["Label"],ToDoListLink=models.ToDoList.objects.get(id=data["ToDoListLink"]),ImageURL=data["ImageURL"],Finished=finishedsave)
        task.save()
        #task = serializers.TagSerializer(data=data)
        #if(task.is_valid(raise_exception=True)):
        #    task.save()
        #print(task.error_messages)
        # newtask = models.Task()
        #ne

        #task.save()

    #newtask.save()
    return Response({
        "data": "clown"
    })