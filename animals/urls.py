
from django.urls import path
from . import views

urlpatterns = [
    path("", views.animal_list, name="animal_list"),
]


from django.urls import path
from . import views

urlpatterns = [
    path("", views.animal_list, name="animal_list"),
    path("add/", views.add_animal, name="add_animal"),
]

