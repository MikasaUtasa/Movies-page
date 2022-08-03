from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


#class User(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)

GRADES = ((0,0),
          (1,1),
          (2,2),
          (3,3),
          (4,4),
          (5,5),
          (6,6),
          (7,7),
          (8,8),
          (9,9),
          (10,10)
          )


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

class Review(models.Model):
    grade = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)], choices=GRADES)
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)


    def __str__(self):
        return "{}'grade".format(self.movie.name)

    #def get_avg(self, movie):
    #    count = len(self.objects.filter(movie=movie))
    #    sm = sum(self.objects.filter(movie=movie))
    #    avg = sm/count
    #    return avg

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
