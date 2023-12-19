from django.views.generic import ListView, DetailView, edit
from django.urls import reverse_lazy, reverse
from .models import Snack


class SnackListView(ListView):
    model = Snack
    template_name = "snacks_list.html"
    context_object_name = "snacks_list"


class SnackDetailView(DetailView):
    template_name = 'snack_detailed.html'
    model = Snack
    context_object_name = 'snack_detailed'


class SnackCreateView(edit.CreateView):
    template_name = 'snack_create.html'
    model = Snack
    context_object_name = "snack_create"
    fields = ["title", "description", "purchaser"]



class SnackDeleteView(edit.DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    context_object_name = "snack_delete"
    success_url = reverse_lazy("snacks_list")


class SnackUpdateView(edit.UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ["title", 'description', "purchaser"]
    context_object_name = "snack_update"
    success_url = reverse_lazy("snacks_list")
