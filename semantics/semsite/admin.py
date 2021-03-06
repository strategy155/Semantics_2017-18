from django.contrib import admin
from .models import HandbookArticle, Idea, Term, Author
from .models import Publication
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(HandbookArticle)
admin.site.register(Idea)
admin.site.register(Term)
admin.site.register(Author, AuthorAdmin)
