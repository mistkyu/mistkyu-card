from django.urls import path
from . import views

urlpatterns = [
		path('', views.news_index, name='news_index'),
		path('create', views.news_create, name='news_create'),
		path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail_view'),
		path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update_view'),
		path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete_view'),
]