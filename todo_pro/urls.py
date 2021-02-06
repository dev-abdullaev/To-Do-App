from django.contrib import admin
from django.urls import path
from todo_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list, name='list'),
    path('update/<str:pk>/', views.updateTask, name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),

]
