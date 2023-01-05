from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

    


class TestPage(TemplateView):
    template_name = "test.html"

class ThankyouPage(TemplateView):
    template_name = "thanks.html" 

