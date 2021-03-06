from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from . import models
from .forms import NameForm
from .models import User, saveDetails


def hello_world(request):
    return render(request, 'index.html', {})


def aboutus(request):
    print("Here")
    return render(request, 'aboutus.html', {})


def post(request):
    post = get_object_or_404(models.Post, pk=1)
    print(post)
    return render(request, 'post.html', {
        'post': post,
    })


def handle(request):
    username = request.POST.get("un", "")
    password = request.POST.get("passwd", "")
    print(username + " " + password)
    try:
        # user = get_object_or_404(models.User, email=username, password=password)
        obj = User.objects.get(email=username, password=password)
    except User.DoesNotExist:
        # raise Http404("No MyModel matches the given query.")
        response = redirect('/')
        return response
    '''if obj is None:
        response = redirect('/')
        return response'''
    request.session['user_name'] = str(obj.name)
    request.session['user_email'] = str(obj.email)
    return render(request, 'homepage.html', {'user': obj})


def show_user(request):
    print("here")
    # u1 = models.User(name="daksh", email="abc", password="123", phone="456")
    # u1.save()
    user = get_object_or_404(models.User, email='priyanshudaksha@yahoo.com')
    print(user.name)
    return render(request, "index.html", {})


def form_handle(request):
    form = NameForm(request.POST)
    return render(request, 'name.html', {'form': form})


def register_page(request):
    return render(request, "Register.html", {})


def register_user(request):
    name = request.POST.get("Username", "")
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")
    phone = request.POST.get("mobile", "")
    u1 = models.User(name=name, email=email, password=password, phone=phone)
    u1.save()
    response = redirect('/')
    return response


def logout_handle(request):
    logout(request)
    return render(request, "logout.html", {})


def enter_data_daily(request):
    time = request.POST.get("time")
    date = request.POST.get("date")
    title = request.POST.get("title")
    detail = request.POST.get("detail")
    name = request.session['user_name']
    email = request.session['user_email']
    print(str(time) + str(date) + title + detail + name)
    details = saveDetails(name=name, email_id=email, date_field=date, title=title, description=detail)
    details.save()
    return render(request, "index.html")
