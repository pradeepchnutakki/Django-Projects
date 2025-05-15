from django.urls import path
from .views import simulate_tree

urlpatterns = [
    path('', simulate_tree, name='simulate_tree'),
]
