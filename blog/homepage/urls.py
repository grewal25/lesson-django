from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    # post views
    path('', views.wall_list, name='wall_list'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    #      views.post_detail,
    #      name='post_detail'),
]