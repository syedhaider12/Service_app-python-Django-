from django.contrib import admin

# Register your models here.
from .models import contact
from .models import bussiness
class displaycontact (admin.ModelAdmin):
     list_display = ('Name', 'email')

class displaybusines (admin.ModelAdmin):
     list_display = ('name', 'price')

admin.site.register(contact, displaycontact)
admin.site.register(bussiness, displaybusines)