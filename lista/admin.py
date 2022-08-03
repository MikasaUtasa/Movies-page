from django.contrib import admin
from .models import Film, Director, Category, Ordered_Item, Order, Ticket, Review

admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Ordered_Item)
admin.site.register(Ticket)
admin.site.register(Review)

# Register your models here.
