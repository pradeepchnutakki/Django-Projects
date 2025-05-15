from django.contrib import admin
from django.urls import path
from simulation import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.simulate_tree, name="simulate_tree"),
    path("tree-data/", views.tree_data, name="tree_data"),
]
