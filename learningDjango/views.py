from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    data ={
        "list" : ["HTML" ,"CSS" ,"JS" , "GIT AND GITHUB" ,"PHP" ,"PYTHON"]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    data = {
        "title":"About Us Page",
    }
    return  render(request,"index.html",data)

def contactUs(request):
    return HttpResponse("This is the contact us page!")

def course(request,course_id):
    return HttpResponse(f"{course_id} : This is the course page!")