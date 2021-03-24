from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('home.html', views.home, name="home"),
	path('contact-us.html', views.contact, name="contact"),
	path('services.html', views.services, name="services"),
	path('about-us.html', views.about, name="about"),
	path('faq.html', views.faq, name="faq"),
	path('news.html', views.news, name="news"),




]
