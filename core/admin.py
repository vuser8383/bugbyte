from django.contrib import admin
from .models import Restaurant, Rating, Sale

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Rating)
admin.site.register(Sale)
