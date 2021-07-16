from django.db import models





# Create your models here.
class User_silkroad(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, default=False)
    password = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    def __str__(self):
        return self.username

class Content(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(blank=True)
    region = models.CharField(max_length=50, null=True, blank=True, choices=(
        ("0", "Чуй"),
        ("1", "Ош"),
        ("2", "Иссык - Куль"),
        ("3", "Баткен"),
        ("4", "Джалал - Абад"),
        ("5", "Нарын")
    ))
    city_or_village = models.CharField(max_length=150, null=True, blank=True)