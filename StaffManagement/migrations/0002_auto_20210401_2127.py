# Generated by Django 3.1.7 on 2021-04-01 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StaffManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Date_of_Birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Designation',
            field=models.CharField(default='Designation', max_length=200),
        ),
        migrations.AddField(
            model_name='staff',
            name='Expertise',
            field=models.TextField(default='Expertise', max_length=200),
        ),
        migrations.AddField(
            model_name='staff',
            name='Profile_Picture',
            field=models.ImageField(blank=True, null=True, upload_to='users/profile_pictures'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='First_Name',
            field=models.ForeignKey(default='Last Name', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
