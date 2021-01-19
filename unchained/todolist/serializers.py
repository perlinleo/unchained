from rest_framework import serializers

from todolist import models

from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    #owner = PrimaryKeyRelatedField(queryset=User.objects.all())
    #ToDoListLink = serializers.ReadOnlyField(source='User.username')
    #TagTaskLink = serializers.ReadOnlyField(source='Task.TagTaskLink')
    #highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = models.Task
        fields = '__all__'
        #use_natural_foreign_keys = True 
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tag
        fields = '__all__'


class ToDoListSerializer(serializers.ModelSerializer):
    #AccountLink = serializers.ReadOnlyField(source='User.username')
    class Meta:
        model = models.ToDoList
        fields = ('id', 'AccountLink', 'Header', 'Description')
    
class UserSerializer(serializers.ModelSerializer):
    #snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

