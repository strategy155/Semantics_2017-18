from django.db import models

class Article(models.Model):
    title = models.Model.CharField(max_length=200)
    main_image = models.ImageField(upload_to="/uploads/")
    text = models.TextField()
    literature = models.ManyToManyField(Publication)
    ideas = models.ManyToManyField(Idea)
    terms = models.ManyToManyField(Term)
