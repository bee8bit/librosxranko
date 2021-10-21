from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

class Author(models.Model):
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autoren"
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name;

class Series(models.Model):
    class Meta:
        verbose_name = "Reihe"
        verbose_name_plural = "Reihen"
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name;

class Medium(models.Model):
    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Medien"
    
    class MediaTypes(models.TextChoices):
        BOOK = 'BOO', _('Buch')
        MAGAZINE = 'MAG', _('Zeitschrift')
        AUDIO_CD = 'CDA', _('Audio-CD')
        CD_ROM = 'CDR', _('CD-ROM')
        AUDIO_CASSETTE = 'CAS', _('Kassette')
        DVD = 'DVD', _('DVD')
        GAME = 'GAM', _('Spiel')
        MULTIPLE = 'MUL', _('mehrere Medien')
        OTHER = 'ZZZ', _('anderes Medium')

    type = models.CharField('Medienart', max_length=3, choices=MediaTypes.choices, default=MediaTypes.BOOK)
    series = models.ForeignKey(Series, verbose_name='gehört zur Reihe', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    series_index_num = models.PositiveSmallIntegerField('Nummer innerhalb der Reihe', blank=True, null=True)
    title_text = models.CharField('Titel', max_length=200, db_index=True, help_text='ggf. Reihe nicht wiederholen')
    authors = models.ManyToManyField(Author, verbose_name='Autor(en)', db_index=True)
    components_num = models.PositiveSmallIntegerField('Anzahl Bestandteile', default=1, help_text='Besteht das Medium aus mehreren Stücken? z.B. Buch mit 2 CDs = 3')
    isbn_ean_text = models.CharField('ISBN/EAN', max_length=13, blank=True)
    cover_image = models.ImageField('Titelbild', upload_to='covers/', blank=True)
    barcode_version_num = models.PositiveSmallIntegerField('Barcode vorhanden', blank=True, null=True, editable=False)

    def __str__(self):
        return self.title_text


