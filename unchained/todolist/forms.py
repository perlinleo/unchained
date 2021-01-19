from django import forms
from todolist.models import *



class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'