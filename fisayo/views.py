from django.shortcuts import render

from .models import Home, About, Profile, Category, Skills, Portfolio, Contact, Details

# Create your views here.
def index(request):

    #Home
    home = Home.objects.latest('updated')

    #About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    #skills
    categories = Category.objects.all()

    #Portfolio
    portfolio = Portfolio.objects.all()

    #Details
    contacts = Contact.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolio': portfolio,
        'contacts': contacts,
    

    }

    return render(request, 'index.html', context)