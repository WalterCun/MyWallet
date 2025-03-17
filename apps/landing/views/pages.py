from django.views.generic import TemplateView

class BlogView(TemplateView):
    template_name = "landing/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RoadmapView(TemplateView):
    template_name = "landing/roadmap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SuggestionsView(TemplateView):
    template_name = "landing/suggestions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context