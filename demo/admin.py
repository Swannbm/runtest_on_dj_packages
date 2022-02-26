from django.contrib import admin

from .models import Person, FavoriteColor


admin.site.register(Person)
admin.site.register(FavoriteColor)
