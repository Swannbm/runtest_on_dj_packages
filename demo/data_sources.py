from django_docx_template import data_sources

from .models import Person


class PersonSource(data_sources.DataSource):
    # properties
    label = "Data source for Person"
    model = Person
    url_args = {"pk": "int"}
    # fields
    first_name = data_sources.Field(examples=["Pierre", "Paul"])
    last_name = data_sources.Field(examples=["Smith", "Dupont"])
    size = data_sources.Field(examples=["180", "190"])
    favorite_color = data_sources.Field(source="color__label", examples=["red", "blue"])
