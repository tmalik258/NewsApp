from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
	path('', views.HomeView.as_view(), name='index'),
	path('article/<int:id>/', views.ArticleView.as_view(), name='article'),
	path('category/<int:id>/', views.CategoryView.as_view(), name='category'),
]