from django.db import models
import django.utils.timezone
from tinymce.models import HTMLField
from publications_bootstrap.models import Publication
from ckeditor.fields import RichTextField


# class Translation(models.Model):
#     language = models.CharField(max_length=200)
#     text = models.CharField(max_length=200)


class IdeaDescriptor:
    def __get__(self, instance, owner):
        return [pub.ideas.all() for pub in instance.publications.all()]


class Term(models.Model):
    name = models.CharField(max_length=200)
    # translations = models.ManyToManyField(Translation)
    translations = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Idea(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    publications = models.ManyToManyField(Publication, blank=True)
    ideas = IdeaDescriptor()
    birthdate = models.DateField(default=django.utils.timezone.now,blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class HandbookArticle(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to="uploads/", blank=True)
    text = RichTextField(config_name='default')
    literature = models.ManyToManyField(Publication, blank=True)
    ideas = models.ManyToManyField(Idea, blank=True)
    terms = models.ManyToManyField(Term, blank=True)

    def __str__(self):
        return self.title
