from django.shortcuts import get_object_or_404, render
from . import models
from .forms import NameForm
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
    return render(request, 'post.html',{})
def show_user(request):
    print("here")
    #u1 = models.User(name="daksh", email="abc", password="123", phone="456")
    #u1.save()
    user = get_object_or_404(models.User, email='priyanshudaksha@yahoo.com')
    print(user.name)
    return render(request, "index.html", {})
def form_handle(request):
    form = NameForm(request.POST)
    return render(request, 'name.html', {'form': form})