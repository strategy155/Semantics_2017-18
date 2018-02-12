from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import HandbookArticle


class IndexView(TemplateView):
    template_name = 'semsite/index.html'


class HandbookView(ListView):
    template_name = 'semsite/handbook.html'
    context_object_name = 'handbook_articles'

    def get_queryset(self):
        return HandbookArticle.objects.all()


class HandbookArticleView(TemplateView):
    template_name = 'semsite/handbook_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['handbook_article'] = get_object_or_404(HandbookArticle, title=kwargs['title'])
        return context

