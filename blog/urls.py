from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('new', views.new_post, name='new'),
    path('detail/<int:pk>', views.detail_post, name="detail"),
]