from email.mime import multipart
from django.shortcuts import render
from pizza.forms import MultiplePizzaForm,PizzaForm

# Create your views here.
def home(request):
    return render(request,"pizza/home.html")

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method=="POST":
        filled_form =PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza=filled_form.save()
            created_pizza_pk=created_pizza.id
            