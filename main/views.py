from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):

	return render(request, 'main/index.html')


def about(request):
	return render(request, 'main/about.html')


def creaters(request):
	tasks = Task.objects.all()
	return render(request, 'main/creaters.html', {'title': tasks})


def news(request):
	return render(request, 'main/news.html')


def donate(request):
	return render(request, 'main/donate.html')	


def heroes(request):
	return render(request, 'main/heroes.html')		