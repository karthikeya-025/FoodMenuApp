from django.urls import path
from . import views

app_name = "menubook"
urlpatterns = [
    path("", views.ClassBasedIndex.as_view(), name="index"),
    path("<int:pk>", views.DetailClassView.as_view(), name="details"),
    path("add/", views.add_item, name="add-item"),
    path("edit/<int:id>", views.update_item, name="update-item"),
    path("delete.<int:id>", views.delete_item, name="delete-item"),
]
