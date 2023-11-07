from django.urls import path, include

from . import views
app_name = 'login'
urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('submit/', views.submit_form, name='submit_form'),
    path('popup/', views.popup, name='popup'),

]
