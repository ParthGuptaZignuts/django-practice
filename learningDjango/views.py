from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("This is the about us page!")

def contactUs(request):
    return HttpResponse("This is the contact us page!")

def course(request,course_id):
    return HttpResponse(f"{course_id} : This is the course page!")