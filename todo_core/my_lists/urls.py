from django.urls import path
from .views import home, items_list


urlpatterns = [
    path("",home),
    path("<pk>/",items_list, name="items_list")
]