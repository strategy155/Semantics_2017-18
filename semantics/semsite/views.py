from django.shortcuts import render, get_object_or_404, get_list_or_404, Http404, reverse
from django.views.generic import TemplateView, ListView, RedirectView
from .models import HandbookArticle


class IndexView(TemplateView):
    template_name = 'semsite/index.html'


class HandbookView(RedirectView):
    pass


    def get_redirect_url(self, *args, **kwargs):
        handbooks = HandbookArticle.objects.all()
        if handbooks:
            self.url = (reverse('handbook_article', kwargs={'title' : handbooks[0].title}))
        return super().get_redirect_url(*args, **kwargs)


class HandbookArticleView(TemplateView):
    template_name = 'semsite/handbook_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['handbook_article'] = get_object_or_404(HandbookArticle, title=kwargs['title'])
        return context

