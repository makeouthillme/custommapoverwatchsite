from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('creaters', views.creaters, name='creaters'),
    path('news', views.news, name='news'),
    path('heroes', views.heroes, name='heroes')
]