from django.views.generic import TemplateView, DetailView
from .models import HandbookArticle, Author, Term, Publication


class IndexView(TemplateView):
    template_name = 'semsite/index.html'


class AuthorView(TemplateView):
    template_name = 'semsite/authors.html'

    def get_context_data(self, **kwargs):
        authors = Author.objects.all()
        alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
        context = super().get_context_data(**kwargs)
        context['authors'] = authors
        context['alphabet'] = alphabet
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'semsite/personality.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        authors = Author.objects.all()

        publications = Publication.objects.all()
        context = super().get_context_data(**kwargs)
        context['authors'] = authors
        context['publications'] = publications
        return context


class HandbookView(TemplateView):
    template_name = 'semsite/handbook.html'

    def get_context_data(self, **kwargs):
        handbook_articles = HandbookArticle.objects.all()
        context = super().get_context_data(**kwargs)
        context['handbook_articles'] = handbook_articles
        context['lit_cl'] = Publication
        return context


class HandbookDetailView(DetailView):
    model = HandbookArticle
    template_name = 'semsite/article.html'
    context_object_name = 'article'
    
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
        alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
        context = super().get_context_data(**kwargs)
        context['terms'] = dictionary
        context['alphabet'] = alphabet
        return context


class DictionaryDetailView(DetailView):
    model = Term
    template_name = 'semsite/termin.html'
    context_object_name = 'term'
    queryset = Term.objects.all()


class LiteratureView(TemplateView):
    template_name = 'semsite/literature.html'

    def get_context_data(self, **kwargs):
        literature = Publication.objects.all()
        alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
        context = super().get_context_data(**kwargs)
        context['literature'] = literature
        context['alphabet'] = alphabet

        return context
