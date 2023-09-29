from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Category, Article

# Create your views here.

class BaseView(TemplateView):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()

		return context


class HomeView(BaseView):
	template_name = 'news/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['articles'] = Article.objects.filter(status='published')

		return context


class ArticleView(BaseView):
	template_name = 'news/article.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['article'] = Article.objects.get(id=self.kwargs['id'])

		return context


class CategoryView(BaseView):
	template_name = 'news/category.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['articles'] = Article.objects.filter(category__id=self.kwargs['id'], status='published')

		return context