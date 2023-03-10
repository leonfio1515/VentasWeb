from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', Inicio.as_view(),name="inicio"),
    path('category_list/', CategoryList.as_view(), name="category_list"),
    path('category_add/', CategoryCreate.as_view(), name="category_add"),
    path('category_edit/<int:pk>', CategoryUpdate.as_view(), name="category_edit"),
    path('category_delete/<int:pk>', CategoryDelete.as_view(), name="category_delete"),

]
