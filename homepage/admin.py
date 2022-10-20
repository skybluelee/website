from django.contrib import admin
from .models import Coffee

# Register your models here.
admin.site.register(Coffee)
# 항상 migration이 필요함
# python manage.py makemigrations homepage
# python manage.py migrate