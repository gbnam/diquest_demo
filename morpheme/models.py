from django.db import models
from konlpy.tag import *


class Sentence(models.Model):
    raw_sentence = models.CharField(max_length=300)
    parsed_sentence = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')


class CsvDocument(models.Model):
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')


class Morpheme(models.Model):
    sentence = models.CharField(max_length=300)
    title = models.CharField(max_length=300)

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
            morpheme_object = Okt()
        return morpheme_object
