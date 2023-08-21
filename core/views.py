from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm

# The function to handle the homepage.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] # Getting the 6 newest unsold products
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

# The function handling the contact page.
def contact(request):
    return render(request, 'core/contact.html',)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })