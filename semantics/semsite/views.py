from django.views.generic import TemplateView
from .models import HandbookArticle, Author, Term, Publication


class IndexView(TemplateView):
    template_name = 'semsite/index.html'

class AuthorView(TemplateView):
    template_name = 'semsite/authors.html'
    def get_context_data(self, **kwargs):
        authors = Author.objects.all()
        context = super().get_context_data(**kwargs)
        context['authors'] = authors
        return context

class HandbookView(TemplateView):
    template_name = 'semsite/handbook.html'


    def get_context_data(self, **kwargs):
        handbook_articles = HandbookArticle.objects.all()
        context = super().get_context_data(**kwargs)
        context['handbook_articles'] = handbook_articles
        context['lit_cl'] = Publication
        return context


class DictionaryView(TemplateView):
    template_name = 'semsite/dictionary.html'

    def get_context_data(self, **kwargs):
        dictionary = Term.objects.all()
        context = super().get_context_data(**kwargs)
        context['terms'] = dictionary
        return context


class LiteratureView(TemplateView):
    template_name = 'semsite/literature.html'

    def get_context_data(self, **kwargs):
        literature = Publication.objects.all()
        context = super().get_context_data(**kwargs)
        context['literature'] = literature

        return context
