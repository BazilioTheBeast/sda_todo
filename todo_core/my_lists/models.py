from django.db.models import Model, CharField, BooleanField, ForeignKey, DateTimeField, CASCADE
from django.contrib.auth.models import User

# Create your models here.


class ToDoList(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    
    def __str__(self):
        return self.title




class ToDoItem(Model):
    name = CharField(max_length=50)
    description = CharField(max_length=200)
    is_completed = BooleanField(default=False)
    todo_list = ForeignKey(ToDoList, on_delete=CASCADE)

    def __str__(self):
        return self.name