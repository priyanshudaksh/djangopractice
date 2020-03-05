from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('about-us', views.aboutus, name="about us"),
    path('post', views.post, name="post"),
    path('handle', views.handle, name="handle"),
    path('user', views.show_user, name="show user"),
    path('form', views.form_handle, name="form"),
    path('Register', views.register_page, name="register"),
    path('register_user', views.register_user, name="register_user"),
]