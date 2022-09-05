from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create_event', views.createEvent, name='create_event'),
    path('pending/', views.pending_request, name='pending'),
    path('update_event/<str:id>', views.update_event, name='update_event'),
    path('results/', views.results, name='results'),
]
