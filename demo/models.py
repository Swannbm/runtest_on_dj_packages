from django.db import models


class FavoriteColor(models.Model):
    label = models.CharField(max_length=30)
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    color = models.ForeignKey(FavoriteColor, on_delete=models.CASCADE, null=True, blank=True)
