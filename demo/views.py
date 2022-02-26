from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

from .models import Person


class PersonCreateView(CreateView):
    model = Person
    fields = ["first_name", "last_name", "birth_date", "size"]
    success_url = reverse_lazy("person:list")


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person
