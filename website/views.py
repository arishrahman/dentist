from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	return render(request, 'contact-us.html', {})


def services(request):
	return render(request, 'services.html', {})


def about(request):
	return render(request, 'about-us.html', {})


def faq(request):
	return render(request, 'faq.html', {})


def news(request):
	return render(request, 'news.html', {})

