from django.db import models

# Create your models here.

class Articles(models.Model):
  title = models.CharField('Title', max_length=50)
  announcement = models.CharField('Announcement', max_length=250)
  article = models.TextField('Article')
  date = models.DateTimeField('Date of publish')
  
  def __str__(self):
      return self.title
    
  def get_absolute_url(self):
      return f'/news/{self.id}'
  
  class Meta:
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'