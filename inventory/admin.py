# In inventory/admin.py

from django.contrib import admin

from .models import Item

#This creates a class that we can pass to admin.site.register that displays selected attributes of a specific object
#from oursite.com/admin
class ItemAdmin(admin.ModelAdmin):
	#What it shows in the splash page for items
	list_display = ['title', 'amount']

#makes our model and it's details appear on admin site
admin.site.register(Item, ItemAdmin)