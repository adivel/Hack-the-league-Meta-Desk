from django.contrib import admin

# Register your models here.
from authentication.models import CustomUser, Card, Resource

admin.site.register(CustomUser)
admin.site.register(Card)
admin.site.register(Resource)