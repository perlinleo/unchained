from django.contrib import admin
from todolist import models


admin.site.register(models.Account)
admin.site.register(models.Tag)
admin.site.register(models.ToDoList)
admin.site.register(models.Task)


# Register your models here.
