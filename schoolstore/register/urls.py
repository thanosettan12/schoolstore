from django.urls import path, include

from . import views
app_name = 'register'

urlpatterns = [

    path('register',views.register ,name='register'),

]
