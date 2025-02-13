from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArticlesForm(ModelForm):
  class Meta:
    model = Articles
    fields = ['title', 'announcement', 'article', 'date']
    
    widgets = {
			'title': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Name of article'
			}),
			'announcement': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Announcement of article'
			}),
			'article': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Text of article'
			}),
   		'date': DateTimeInput(attrs={
        'class': 'form-control',
				'placeholder': 'Date of article (XXXX-XX-XX XX:XX)'
			}),
		}