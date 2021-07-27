
from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('', views.index, name="index"),
    path('person_new', views.person_new, name="person_new"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]