from django.db import models


# class Translation(models.Model):
#     language = models.CharField(max_length=200)
#     text = models.CharField(max_length=200)


class IdeaDescriptor:
    def __get__(self, instance, owner):
        return [pub.ideas.all() for pub in instance.publications.all()]


class Term(models.Model):
    name = models.CharField(max_length=200)
    # translations = models.ManyToManyField(Translation)
    translations = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name



class Dictionary(models.Model):
    terms = models.ManyToManyField(Term, blank=True)


class Idea(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Publication(models.Model):
    name = models.CharField(max_length=30)
    ideas = models.ManyToManyField(Idea, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    photo = models.ImageField(upload_to='uploads/', blank=True)
    publications = models.ManyToManyField(Publication)
    ideas = IdeaDescriptor()

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class HandbookArticle(models.Model):
    title = models.CharField(max_length=200)
    urlname = models.CharField(max_length=200, blank=True)
    main_image = models.ImageField(upload_to="uploads/", blank=True)
    text = models.TextField()
    literature = models.ManyToManyField(Publication, blank=True)
    ideas = models.ManyToManyField(Idea, blank=True)
    terms = models.ManyToManyField(Term, blank=True)

    def __str__(self):
        return self.title
