from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.RecipeList.as_view(), name='list'),
    path('<int:pk>/', views.RecipeDetail.as_view(), name='detail'),
    path('create/', views.RecipeCreate.as_view(), name='create'),
]