from django.db import models
from django.contrib.auth.models import User



#class User(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)




class Director(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=200)
    #ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rel_date = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(max_length=1000)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Ticket(models.Model):
    movie = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True, related_name='ticket')
    price = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{}'s ticket".format(self.movie.name)

class Ordered_Item(models.Model):
    product = models.OneToOneField(Ticket, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.product.movie.name)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Ordered_Item)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s order".format(self.owner)

    def get_itmes(self):
        return self.items.all()

    def get_total(self):
        return sum([item.product.price for item in self.items.all()])







# Create your models here.
