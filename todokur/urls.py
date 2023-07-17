from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('signup/', views.signupuser, name='signupuser'),
    path('current/', views.todocurrent, name='todocurrent'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('home/', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('', views.redirecttohome, name='redirecthome')
]
