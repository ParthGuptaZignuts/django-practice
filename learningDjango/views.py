from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        "title": "Home Page",
        "list": ["HTML", "CSS", "JS", "GIT AND GITHUB", "PHP", "PYTHON"]
    }
    return render(request, "SecondFile.html", data)

def aboutUs(request):
    data = {
        "title": "About Us Page",
    }
    return render(request, "index.html", data)

def contactUs(request):
    data = {
        "title": "Contact Us Page",
        "items": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, "index.html", data)

def course(request, course_id):
    return HttpResponse(f"{course_id}: This is the course page!")
