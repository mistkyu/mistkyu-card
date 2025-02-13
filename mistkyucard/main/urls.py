from django.urls import path
from . import views

urlpatterns = [
		path('', views.main_index, name='home'),
		path('about', views.main_about, name='about'),
		path('socials', views.main_socials, name='socials'),
		path('contacts', views.main_contacts, name='contacts'),
]