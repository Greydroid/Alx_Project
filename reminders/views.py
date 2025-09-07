from django.shortcuts import render

def reminder_list(request):
    return render(request, 'reminders/reminder_list.html')

