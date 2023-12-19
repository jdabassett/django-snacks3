from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path("create", SnackCreateView.as_view(), name="snack_create"),
    path("snacks", SnackListView.as_view(), name="snacks_list"),
    path("snacks/<int:pk>", SnackDetailView.as_view(), name="snack_detailed"),
    path("snacks/<int:pk>/delete", SnackDeleteView.as_view(), name="snack_delete"),
    path("snacks/<int:pk>/update", SnackUpdateView.as_view(), name="snack_update"),
]
