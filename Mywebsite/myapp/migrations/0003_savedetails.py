# Generated by Django 3.0.3 on 2020-03-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200304_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='saveDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('date_field', models.DateField()),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]