# Importing Generic View
from django.views.generic import (TemplateView)


# a view for accessing test.html
class Test(TemplateView):
    template_name = 'test.html'

# a view for accessing thanks.html
class ThankYou(TemplateView):
    template_name = 'thanks.html'

# a view for Home page
class HomePage(TemplateView):
    # accessing the index html since it's the homepage
    template_name = 'index.html'