from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnimalForm

def animal_list(request):
    return HttpResponse("Here will be the list of animals")


from django.shortcuts import render
from .models import Animal

def animal_list(request):
    animals = Animal.objects.all()  # fetch all animals
    return render(request, "animals/list.html", {"animals": animals})


from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, "animals/list.html", {"animals": animals})

def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animal_list")
    else:
        form = AnimalForm()
    return render(request, "animals/add.html", {"form": form})


from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, "animals/list.html", {"animals": animals})

def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animal_list")
    else:
        form = AnimalForm()
    return render(request, "animals/add.html", {"form": form})


