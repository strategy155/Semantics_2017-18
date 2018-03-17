from django.db import models
import django.utils.timezone
from publications_bootstrap.models import Publication
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import unidecode

# class Translation(models.Model):
#     language = models.CharField(max_length=200)
#     text = models.CharField(max_length=200)


class IdeaDescriptor:
    def __get__(self, instance, owner):
        return [pub.ideas.all() for pub in instance.publications.all()]


class Term(models.Model):
    class Meta:
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'

    # letter = models.CharField(max_length=200)
    # translations = models.ManyToManyField(Translation)
    # translations = models.TextField(blank=True)

    name = models.CharField(max_length=200, verbose_name="Название", 
        help_text="Если у термина несколько названий, разделяйте их запятыми")
    description = models.TextField(blank=False, verbose_name="Определение")

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        self.get_names()

    def get_names(self):
        self.name = self.name.replace(', and ', ', ')
        self.name = self.name.replace(',and ', ', ')
        self.name = self.name.replace(' and ', ', ')
        self.name = self.name.replace(';', ',')
        self.names = [author.strip() for author in self.name.split(',')]

    def __str__(self):
        return self.name


class Idea(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    publications = models.ManyToManyField(Publication, blank=True)
    ideas = IdeaDescriptor()
    birthdate = models.DateField(default=django.utils.timezone.now,blank=False)
    slug = models.SlugField(blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode.unidecode(self.first_name +' ' +self.last_name))
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'




class HandbookArticle(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to="uploads/", blank=True)
    literature = models.ManyToManyField(Publication, blank=True)
    text = RichTextField(config_name='default')
    ideas = models.ManyToManyField(Idea, blank=True)
    terms = models.ManyToManyField(Term, blank=True)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.title
