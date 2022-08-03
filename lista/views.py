from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Film, Director, Order, Ordered_Item , Category, Ticket, Review, GRADES
from django.template import loader
from django.http import Http404
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from lista.forms import VoteForm

def main(request):
    return render(request, 'main.html')

def user(request):
    order = Order.objects.filter(owner=request.user).first()
    cart_list = order.get_itmes()
    total = order.get_total()
    #cart_list = order.items.order_by('product')
    context = {'cart_list': cart_list,
               'total': total}
    return render(request, 'user_panel.html', context)

def list(request):
    movie_list = Film.objects.order_by('name')
    #price_list = Ticket.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'index2.html', context)

def Search(request):
    query = request.GET.get("q")
    movie_list = Film.objects.filter(Q(name__icontains=query) )
    context = {'movie_list': movie_list}
    return render(request, 'search_result.html', context)


def director_list(request):
    movie_list = Film.objects.order_by('director')
    context = {'movie_list': movie_list}
    return render(request, 'director.html', context)

def detail(request, movie_id, **kwargs):

    if request.method == 'GET':
        try:
            movie1 = Film.objects.get(pk=movie_id)
            try:
                ticket = Ticket.objects.get(movie=movie1)
                price = ticket.price
                grades = Review.objects.filter(movie__id=movie_id).all()
                #avg_grade = grades.get_avg(movie1)
                sumg = 0
                try:
                    for grade in grades:
                        sumg += grade.grade
                    avg = sumg / len(grades)
                except:
                    avg = '-'
            except Ticket.DoesNotExist:
                price = '-'
        except Film.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'detail.html',
                      {
                          'movie': movie1, 'price': price,
                          'date': movie1.rel_date,
                          'director': movie1.director,
                          'description': movie1.description,
                          'category': movie1.category.all(),
                          'grade': avg,
                          'form': VoteForm,
                      })
    elif request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/main/{}/'.format(movie_id))
        else:
            return HttpResponseRedirect('/main/')


def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {"form": CustomUserCreationForm})

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user1 = form.save()
            login(request, user1)
            return redirect(reverse("list"))

@login_required()
def cart_add(request, movie_id, **kwargs):
    if request.user.is_authenticated:
        user = request.user
        movie = Film.objects.filter(id=movie_id).first()
        product1 = Ticket.objects.filter(movie__name=movie).first()
        ordered_item, created = Ordered_Item.objects.get_or_create(product=product1)
        user_order, status = Order.objects.get_or_create(owner=user)
        user_order.items.add(ordered_item)
        #if status:
        #    user_order.save()
        #    return redirect(reverse("main"))
        #else:
        messages.info(request, 'item added to cart')
        return redirect(reverse("list"))

@login_required()
def cart_delete(request, movie_id):
    item_to_delete = Ordered_Item.objects.filter(product__movie__id=movie_id).first()
    item_to_delete.delete()
    return redirect(reverse("user_panel"))




# Create your views here.
