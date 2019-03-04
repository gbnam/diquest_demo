from django.db import models


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
