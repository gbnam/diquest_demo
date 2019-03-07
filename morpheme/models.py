from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from konlpy.tag import *


class Sentence(models.Model):
    raw_sentence = models.CharField(max_length=300)
    parsed_sentence = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    class Meta:
        verbose_name = 'sentence'
        verbose_name_plural = 'sentences'
        db_table = 'morpheme_sentence'


class CsvDocument(models.Model):
    file_morpheme_type = models.CharField(max_length=1, choices=(
        ('', u'선택'),
        ('mecab', u'mecab'),
        ('jiana', u'jiana'),
        ('kkma', u'kkma'),
        ('komoran', u'komoran'),
        ('okt', u'okt'),
        ('hannanum', u'hannanum')
    ))
    file = models.FileField(
        upload_to='files/%Y/%m',
        name='file',
        default=None,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["csv"], message="CSV 파일만 허용 가능")]
    )

    class Meta:
        verbose_name = 'csvdocument'
        verbose_name_plural = 'csvdocuments'
        db_table = 'morpheme_csvdocument'


class Morpheme(models.Model):
    sentence = models.CharField(max_length=300)
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'morpheme'
        verbose_name_plural = 'morphemes'
        db_table = 'morpheme_morpheme'

    @staticmethod
    def morpheme_init(morpheme_type):
        morpheme_object = None
        if morpheme_type == 'mecab':
            morpheme_object = Okt()
        elif morpheme_type == 'okt':
            morpheme_object = Okt()
        elif morpheme_type == 'komoran':
            morpheme_object = Komoran()
        elif morpheme_type == 'hannanum':
            morpheme_object = Hannanum()
        elif morpheme_type == 'kkma':
            morpheme_object = Kkma()
        elif morpheme_type == 'jiana':
            # morpheme_object = Jiana()
            morpheme_object = Okt()

        return morpheme_object

    @staticmethod
    def pos_list(obj, data_frame):
        for j in range(len(data_frame)):
            doc_number = str(data_frame['docNumber'][j])
            speaker_type = data_frame['speakerType'][j]
            sentence = data_frame['sentence'][j]
            yield [doc_number, speaker_type, obj.pos(sentence)]
