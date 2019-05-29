from django.urls import path
from django.contrib.auth import views as auth_views
from food.views import ResearchView

from . import views


app_name = 'food'
urlpatterns = [
    path('results/', ResearchView.as_view(), name='result_page'),
    path('food/<int:food_id>/', views.food_page, name='food_detail'),
    path('ajax/', views.favorite, name='favorite'),
    path('myfoods/', views.my_foods, name='foods_saved')
]