from django.contrib import admin
from .models import Author, Series, Medium

class MediaAdmin(admin.ModelAdmin):
    filter_horizontal = ('authors',)

admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Medium, MediaAdmin)

