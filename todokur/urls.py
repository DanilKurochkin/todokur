from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    
    
    path('', views.redirecttohome, name='redirecthome'),
    path('current/', views.todocurrent, name='todocurrent'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='todocreate'),
    path('completed/', views.todocompleted, name = 'todocompleted'),
    path('todo/<int:todo_pk>', views.viewtodo, name = 'viewtodo')
]
    