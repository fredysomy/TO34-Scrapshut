from django.contrib import admin
from .models import User,Products,ProductQuery
# Register your models here.
admin.site.register(User)
admin.site.register(Products)
admin.site.register(ProductQuery)