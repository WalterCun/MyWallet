from django.urls import path
from ..views.pages import RoadmapView

urlpatterns = [
    path('', RoadmapView.as_view(), name='roadmap'),
]