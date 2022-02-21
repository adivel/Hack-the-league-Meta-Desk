from django.contrib import admin

# Register your models here.
from user_view.models import Resource, Card

admin.site.register(Card)
admin.site.register(Resource)