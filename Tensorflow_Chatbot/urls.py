from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Userlogin, name='login'),
    path('chat/', views.chat, name='chat'),
    path('api', include("Tensorflow_Chatbot.Api.urls")),
    path('logout/', views.Userlogout, name='logout'),
]
