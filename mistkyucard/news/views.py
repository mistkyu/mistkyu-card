from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def news_index(request):
	news = Articles.objects.order_by('-date')
	return render(request, 'news/index.html', {'news': news})

class NewsDetailView(DetailView):
  model = Articles
  template_name = 'news/details_view.html'
  context_object_name = 'article'

class NewsUpdateView(UpdateView):
  model = Articles
  template_name = 'news/update.html'
  form_class = ArticlesForm
  
class NewsDeleteView(DeleteView):
  model = Articles
  success_url = '/news/'
  template_name = 'news/delete.html'
  
def news_create(request):
  error = ''
  if request.method == 'POST':
    form = ArticlesForm(request.POST) 
    if form.is_valid():
      form.save()
      return redirect('news_index')
    else:
      error = 'Form was invalid'
      
  
  form = ArticlesForm
  
  data = {
		'form' : form,
    'error': error,
	}
  return render(request, 'news/create.html', data)