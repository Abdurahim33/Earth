from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from About.models import Backround_image, About_model
from django.views.generic import ListView


class About_view(ListView):
    template_name = 'about.html'


    def get_queryset(self) -> QuerySet[Any]:
        q = Backround_image.objects.all()
        return q
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['About'] = About_model.objects.all()
        return data