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
    if request.method == 'GET':
        user_email = request.GET.get('UserEmail')
        user_password = request.GET.get('UserPassword')
        if user_email and user_password:
            print(f"Email: {user_email}, Password: {user_password}")
            return HttpResponse("Form submitted successfully!")

    return render(request, "Contact.html")

def course(request, course_id):
    return HttpResponse(f"{course_id}: This is the course page!")
