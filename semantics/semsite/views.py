from django.shortcuts import render, get_object_or_404, get_list_or_404, Http404, reverse
from django.views.generic import TemplateView, ListView, RedirectView
from .models import HandbookArticle, Person


class IndexView(TemplateView):
    template_name = 'semsite/index.html'

class AuthorView(ListView):
    template_name = 'semsite/authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Person.objects.order_by('birthdate').all()


class HandbookView(TemplateView):
    template_name = 'semsite/handbook.html'

    def get_context_data(self, **kwargs):
        handbook_articles = HandbookArticle.objects.all()
        context = super().get_context_data(**kwargs)
        context['handbook_articles'] = handbook_articles
        return context

