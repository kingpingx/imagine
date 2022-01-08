from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

def home(request):
    return redirect('login/')

def login(request):
    return render(request, 'base.html')