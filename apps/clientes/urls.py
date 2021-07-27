
from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('clientes', views.clientes, name="clientes"),
    path('documentos', views.documentos, name="documentos"),
    path('person_new', views.person_new, name="person_new"),
    path('doc_new', views.doc_new, name="doc_new"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update_doc/<int:id>/', views.update_doc, name="update_doc"),
    path('delete_doc/<int:id>/', views.delete_doc, name="delete_doc"),
]