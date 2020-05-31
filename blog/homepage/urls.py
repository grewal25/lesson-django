from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    # post views
    path('index/', views.index, name = 'index'),
    path('', views.wall_list, name='wall_list'),

    path('<int:publisher_id>/',
         views.wall_detail, name='wall_detail'),
]