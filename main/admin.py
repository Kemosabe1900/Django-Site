from django.contrib import admin
from .models import ToDoList,Item
# Register your models here.
#username: matinemera
#password: 12345
admin.site.register(ToDoList)
admin.site.register(Item)