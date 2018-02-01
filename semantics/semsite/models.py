from django.db import models

# Create your models here.


# class Translation(models.Model):
#     language = models.CharField(max_length=200)
#     text = models.CharField(max_length=200)


class IdeaDescriptor:
    def __get__(self, instance, owner):
        return [pub.ideas.all() for pub in instance.publications.all()]


class Term(models.Model):
    name = models.CharField(max_length=200)
    #translations = models.ManyToManyField(Translation)
    translations = models.TextField()
    description = models.TextField()


class Dictionary(models.Model):
    terms = models.ManyToManyField(Term)


class Idea(models.Model):
    name = models.CharField(max_length=30)


class Publication(models.Model):
    name = models.CharField(max_length=30)
    ideas = models.ManyToManyField(Idea)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    publications = models.ManyToManyField(Publication)
    ideas = IdeaDescriptor()
