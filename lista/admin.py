from django.contrib import admin
from .models import Film, Director, Category, Ordered_Item, Order, Ticket

admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Ordered_Item)
admin.site.register(Ticket)

# Register your models here.
