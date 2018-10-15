from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/recipe', views.form_name_view, name='form_name_view'),
    path('edit/', views.recipe_edit, name='edit'),

]