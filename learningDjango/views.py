from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import NumberForm

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

def formPostMethod(request):
    if request.method == 'POST':
        user_email = request.POST.get('UserEmail')
        user_password = request.POST.get('UserPassword')
        
        if user_email and user_password:
            print(f"Email: {user_email}, Password: {user_password}")
            return HttpResponseRedirect("/")

   
    return render(request, "formPostMethod.html")

def oddOrEven(request):
    result = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['num']
            if number % 2 == 0:
                result = f"{number} is even."
            else:
                result = f"{number} is odd."
    else:
        form = NumberForm()

    return render(request, 'oddOrEven.html', {'form': form, 'result': result})
