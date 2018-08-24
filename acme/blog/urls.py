from django.urls import path
from . import views
from . import views as auth_views

app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    #path('toto/<id>', views.show, name='show'),
    path('t/<id>', views.show, name='show'),
    path('register/', views.UserFormView.as_view(), name='register'),

    path('login/', views.user_login, name='login'),
    path('logout/',  auth_views.user_logout, name='logout'),
]
