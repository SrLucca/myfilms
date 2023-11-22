from django.urls import path
from main import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('edit/<int:id>', views.editMovie, name="editmovie"),
    path('import_sheet', views.importSheet, name="importsheet")
]