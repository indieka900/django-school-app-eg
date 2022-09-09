from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
	path('students/', views.ourList, name="students"),
	path('student/<str:pk>/', views.viewStudi, name="viewStudi"),
	path('delete/<str:pk>/', views.deleteStudi, name="deleteStudi"),
	path('update/<str:pk>/', views.updateStudi, name="updateStudi"),
]