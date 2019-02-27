from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tagging.fields import TagField
import os


class Support(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()
    attach_file = models.FileField(
        upload_to='files/%Y/%m',
        name='file',
        default=None,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["pdf", "zip"], message="Zip 또는 PDF 파일만 허용 가능")]
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'support'
        verbose_name_plural = 'supports'
        db_table = 'support_details'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('support:support_detail', args=(self.slug,))

    def get_previous_support(self):
        return self.get_previous_by_modify_date()

    def get_next_support(self):
        return self.get_next_by_modify_date()

    def get_file_absolute_url(self):
        return self.file.url

    def get_file_pdf_id_url(self):
        return reverse('support:support_pdf_viewer', args=(self.id,))

    def get_file_extension(self):
        _, extension = os.path.splitext(self.file.name)
        return extension.replace('.', '')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Support, self).save(*args, **kwargs)
