from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "date_time": strftime("%b %d %Y %I:%M%p", gmtime())
    }
    return render(request, 'time_display/index.html', context)


