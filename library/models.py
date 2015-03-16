from django.db import models
from django.template.defaultfilters import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth = models.DateField()
    wiki = models.URLField()

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title