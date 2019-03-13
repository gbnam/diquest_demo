from django.contrib import admin

from .models import MorphemeAnalysisModel


class MorphemeAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'raw_sentence', 'morpheme_type', 'file', 'reg_date', 'user_name')


admin.site.register(MorphemeAnalysisModel, MorphemeAdmin)
