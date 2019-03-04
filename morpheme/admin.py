from django.contrib import admin

from .models import Morpheme


class MorphemeAdmin(admin.ModelAdmin):
    list_display = ('sentence', 'title')


admin.site.register(Morpheme, MorphemeAdmin)
