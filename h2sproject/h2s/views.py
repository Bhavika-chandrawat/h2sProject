from django.shortcuts import render

# Create your views here.
def SignUp(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user_create=User.