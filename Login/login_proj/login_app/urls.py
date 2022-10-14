from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('components/', views.components, name='components'),

]
