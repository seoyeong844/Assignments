from django.shortcuts import render

# Create your views here.

def introducing(request):
    return render(request, 'introducing.html')