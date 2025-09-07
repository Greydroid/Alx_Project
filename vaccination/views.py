from django.shortcuts import render

def vaccination_list(request):
    return render(request, 'vaccination/vaccination_list.html')

