# Test django packages

This project aims to test all the django packages you have published.

## Create Symlink to your package

Let say you have a django package here : `~/django-app-parameter`, with the following directories organisation:

    django-app-parameter
       |-- django_app_parameter

All what needs to be tested should be on the subfolder with underscores.

To run test correctly, you can add it to this current Django project with a Symbolic link: `ln -s ~/django-app-parameter/django_app_parameter .`

Then you need to setup correctling settings.py and all what is required to test it.
