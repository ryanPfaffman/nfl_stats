from django.contrib import admin

# Register your models here.
from .models import Qb, Rb, Defense

admin.site.register(Qb)
admin.site.register(Rb)
admin.site.register(Defense)
