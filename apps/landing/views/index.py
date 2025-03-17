from django.shortcuts import render
from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "landing/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
