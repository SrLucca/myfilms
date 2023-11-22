from django.db import models

# Create your models here.
GENDERS = (
    ('Comédia','Comédia'),
    ('Terror','Terror'),
    ('Drama','Drama'),
    ('Romance','Romance'),
    ('Ação','Ação'),
    ('Infantil','Infantil'),
)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    watched_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDERS)
    wish_list = models.BooleanField(default=False)

    def __str__(self):
        return self.title