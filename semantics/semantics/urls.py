"""semantics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from semsite.views import IndexView, HandbookView, AuthorView, DictionaryView, \
LiteratureView, DictionaryDetailView, AuthorDetailView, HandbookDetailView, LiteratureDetailView
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    path('authors/', AuthorView.as_view(), name='authors'),
    url(r'^authors/(?P<slug>[\w-]+)$', AuthorDetailView.as_view(), name='personality'),
    path('handbook/', HandbookView.as_view(), name='handbook'),
    url(r'^handbook/(?P<slug>[\w-]+)$', HandbookDetailView.as_view(), name='article'),
    path('dictionary/', DictionaryView.as_view(), name='dictionary'),
    url(r'^dictionary/(?P<slug>[\w-]+)$', DictionaryDetailView.as_view(), name='termin'),
    path('literature/', LiteratureView.as_view(), name='literature'),
    url(r'^literature/(?P<pk>\d+)$', LiteratureDetailView.as_view(), name='book'),
    # url(r'^publications/', include('publications_bootstrap.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
