from django.db import models
import django.utils.timezone
from ckeditor.fields import RichTextField
from publications_bootstrap.models import Publication
from django.utils.text import slugify
import unidecode
from django.db import connection
from autoslug import AutoSlugField

# class Translation(models.Model):
#     language = models.CharField(max_length=200)
#     text = models.CharField(max_length=200)


class IdeaDescriptor:
    def __get__(self, instance, owner):
        return [pub.ideas.all() for pub in instance.publications.all()]




class Term(models.Model):
    def slugify(self):
        return slugify(unidecode.unidecode(self.name))

    class Meta:
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'

    # letter = models.CharField(max_length=200)
    # translations = models.ManyToManyField(Translation)
    # translations = models.TextField(blank=True)

    name = models.CharField(max_length=200, verbose_name="Название", 
        help_text="Если у термина несколько названий, разделяйте их запятыми")
    description = RichTextField(blank=False, verbose_name="Определение",config_name='default')
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from=slugify)


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
        return self.names[0]


class Idea(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'


class Author(models.Model):
    def slugify(self):
        new_name = slugify(unidecode.unidecode(self.first_name + '-' + self.last_name))
        print(new_name)
        with connection.cursor() as cursor:
            cursor.execute("UPDATE semsite_author SET slug = %s WHERE first_name = %s AND last_name = %s", [new_name, self.first_name, self.last_name])
            cursor.execute("SELECT * FROM semsite_author")
            print(cursor.fetchall())

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = RichTextField(blank=True,config_name='default')
    photo = models.ImageField(upload_to='uploads/', blank=True)
    publications = models.ManyToManyField(Publication, blank=True)
    ideas = IdeaDescriptor()
    birthdate = models.DateField(default=django.utils.timezone.now,blank=False)

    with connection.cursor() as cursor:
        cursor.execute("pragma table_info(semsite_author)")
        column_names = [col[1] for col in cursor.fetchall()]
        if "slug" in column_names:
            pass
        else:
            cursor.execute("ALTER TABLE semsite_author ADD COLUMN slug TEXT;")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)
        self.slugify()


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'





class HandbookArticle(models.Model):
    def slugify(self):
        return slugify(unidecode.unidecode(self.title))

    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to="uploads/", blank=True)
    literature = models.ManyToManyField(Publication, blank=True)
    chapters = models.TextField(verbose_name="Оглавление", 
        help_text="Названия разделов должны писаться через $ и пробел, например 'Глава 1$ Глава 2'")
    text = RichTextField(config_name='default')
    ideas = models.ManyToManyField(Idea, blank=True)
    terms = models.ManyToManyField(Term, blank=True)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from=slugify)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.title
