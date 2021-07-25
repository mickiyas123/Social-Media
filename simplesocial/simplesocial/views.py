# Importing Generic View
from django.views.generic import (TemplateView)

# a view for Home page
class HomePage(TemplateView):
    # accessing the index html since it's the homepage
    template_name = 'index.html'