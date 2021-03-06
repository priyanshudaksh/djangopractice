from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    author_name = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)


class saveDetails(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    date_field = models.DateField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
