from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is homepage (/)")
    content = {'name': 'SJD'}
    return render(request, 'home.html', content)

def about(request):
    content = {
        'title': 'About',
    }
    return render(request, 'about.html', content)

def projects(request):
    content = {
        'title': 'Projects',
    }
    return render(request, 'projects.html', content)

def contact(request):
    content = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', content)
