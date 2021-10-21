from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

class Lending(models.Model):
    class Meta:
        verbose_name="Klasse"
        verbose_name_plural="Klassen"
    
    name = models.CharField(max_length=50)
    group_admin = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True, related_name="+", limit_choices_to={'role': 'TEA'})
    
    def __str__(self):
      if self.group_admin:
          return self.name + " (" + self.group_admin.name + ")"
      else:
          return self.name
