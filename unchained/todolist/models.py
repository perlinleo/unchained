from django.db import models

from django.contrib.auth.models import User


#EntityRelations.html related

class Account(models.Model):
    UserLink = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="UserAccountLink")
    DateCreated = models.TimeField(auto_now_add=True, blank=True,verbose_name="Date created")
    UserName = models.CharField(max_length=32, verbose_name="Username")
    

    def __str__(self):
        return self.UserLink.get_username()
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

class ToDoList(models.Model):
    AccountLink = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="ToDoListAccountLink")
    Header = models.CharField(max_length=64,verbose_name="Header")
    Description = models.TextField(verbose_name="Description")
    def __str__(self):
        return f"{self.AccountLink.UserLink.get_username()}`s {self.Header} list"
    class Meta:
        verbose_name = 'ToDo List'
        verbose_name_plural = 'ToDo Lists'



class Tag(models.Model):
    IconURL = models.URLField(verbose_name="IconURL")
    Label = models.CharField(max_length=32, verbose_name="Label",blank=True)
    def __str__(self):
        return self.Label
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Task(models.Model):
    ToDoListLink = models.ForeignKey(ToDoList, on_delete= models.CASCADE, verbose_name="ToDoListTaskLink",blank=True)
    Finished = models.BooleanField(verbose_name="Finished?",blank=True,default=False)
    TimeAdded = models.TimeField(auto_now_add=True, blank=True,verbose_name="Time added")
    Label = models.CharField(max_length=32,blank=True, verbose_name="Label")
    Description = models.TextField(blank=True,verbose_name="Description")
    ImageURL = models.URLField(blank=True,verbose_name="ImageURL")
    TagTaskLink = models.ManyToManyField(Tag,blank=True,verbose_name="TagTaskLink")
    def __str__(self):
        return f"Task <{self.Label}> of {self.ToDoListLink.AccountLink.UserLink.get_username()}`s {self.ToDoListLink.Header} list"
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


    

    