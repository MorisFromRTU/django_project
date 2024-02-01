from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import BlogPost, Student, Group
from django.template import Context
from django.utils import timezone
from django.contrib.auth.models import User


def create_blogpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        timestamp = request.POST.get('timestamp')

        # Convert the timestamp string to a datetime object
        timestamp = timezone.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M')

        # Create a new BlogPost instance
        new_blogpost = BlogPost(title=title, body=body, timestamp=timestamp)

        # Save the instance to the database
        new_blogpost.save()

    # Render the form template for GET requests
    return render(request, 'main/record.html')
def show_blogpost(request):
    all_objects = BlogPost.objects.all()
    return render(request, 'main/show.html', {'all_objects': all_objects})

def show_results(request):
    query = request.GET.get('query', '')
    filtered_objects = BlogPost.objects.all().filter(title__icontains=query)
    return render(request, 'main/show.html', {'all_objects' : filtered_objects})

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'main/index.html', {'post' : posts})
    # return HttpResponse("<h4>Main Page</h4>")

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        surname = request.POST.get('last_name')
        login = request.POST.get('username')
        group_num = request.POST.get('group')
        password = request.POST.get('password')
        group = Group.objects.get(number=group_num)
        user = User.objects.create(first_name=name, last_name=surname, username=login, password=password)
        new_student = Student(user=user, group_id=group.id)
        new_student.save()
    return render(request, 'main/registration.html')

def group_registration(request):
    if request.method == 'POST':
        number = request.POST.get('group_number')
        new_group = Group(number=number)
        new_group.save()
    return render(request, 'main/registration.html')