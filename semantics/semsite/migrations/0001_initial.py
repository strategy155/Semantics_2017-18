<<<<<<< HEAD
# Generated by Django 2.0.2 on 2018-03-14 17:18

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone

=======
# Generated by Django 2.0.2 on 2018-02-14 10:07

from django.db import migrations, models
import django.utils.timezone
import ckeditor
>>>>>>> 823271ab7b8f190dad57bf5bdebcd37b4091d246

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications_bootstrap', '0005_alter_pdf_field'),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='uploads/')),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('publications', models.ManyToManyField(blank=True, to='publications_bootstrap.Publication')),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 823271ab7b8f190dad57bf5bdebcd37b4091d246
            name='HandbookArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_image', models.ImageField(blank=True, upload_to='uploads/')),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('translations', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='handbookarticle',
            name='ideas',
            field=models.ManyToManyField(blank=True, to='semsite.Idea'),
        ),
        migrations.AddField(
            model_name='handbookarticle',
            name='literature',
            field=models.ManyToManyField(blank=True, to='publications_bootstrap.Publication'),
        ),
        migrations.AddField(
            model_name='handbookarticle',
            name='terms',
            field=models.ManyToManyField(blank=True, to='semsite.Term'),
        ),
    ]
