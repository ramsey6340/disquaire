from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2022)])
    active = models.fields.BooleanField(default=True)
    official_home_page = models.fields.URLField(blank=True, null=True)

    # définition de la classe Genre pour le genre de bande
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    # ==================FIN==================
    # définition de la classe Genre pour le genre de bande
    class Statuts(models.TextChoices):
        NOUVEAU = 'New'
        ANCIEN = 'old'
    # ==================FIN==================
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    statuts = models.fields.CharField(choices=Statuts.choices, max_length=5)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)

    # définition de la classe Type pour le type d'article
    class Type(models.TextChoices):
        RECORDS = 'records'
        CLOTHING = 'clothing'
        POSTERS = 'posters'
        MISCELLANEOUS = 'miscellaneous'
    # ==================FIN==================
    type = models.fields.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'

