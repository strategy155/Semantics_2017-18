from django.contrib import admin
from .models import HandbookArticle, Publication, Idea, Term, Person, Dictionary

# Register your models here.

admin.site.register(HandbookArticle)
admin.site.register(Publication)
admin.site.register(Idea)
admin.site.register(Term)
admin.site.register(Person)
admin.site.register(Dictionary)