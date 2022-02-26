from django.urls import path

from . import views


app_name = "person"


urlpatterns = [
    path("", views.PersonListView.as_view(), name="list"),
    path("<int:pk>", views.PersonDetailView.as_view(), name="detail"),
    path("create", views.PersonCreateView.as_view(), name="create"),
]
