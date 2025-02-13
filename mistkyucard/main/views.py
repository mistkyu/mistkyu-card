from django.shortcuts import render
# Create your views here.

def main_index(request):
  return render(request, 'main/index.html')

def main_about(request):
  return render(request, 'main/about.html')

def main_socials(request):
  return render(request, 'main/socials.html')

def main_contacts(request):
  return render(request, 'main/contacts.html')