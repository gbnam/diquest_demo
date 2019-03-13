from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from konlpy.tag import *
import uuid

morpheme_lists = (
    ('', u'선택'),
    ('mecab', u'mecab'),
    ('jiana', u'jiana'),
    ('kkma', u'kkma'),
    ('komoran', u'komoran'),
    ('okt', u'okt'),
    ('hannanum', u'hannanum')
)

date_input_format = ['%Y-%m-%d %H:%M:%S']


class MorphemeAnalysisModel(models.Model):
    auto_increment_id = models.AutoField(primary_key=True, default=uuid.uuid1)
    raw_sentence = models.CharField(max_length=300, verbose_name='원문 문장', name='raw_sentence')
    slug = models.SlugField(unique=True, allow_unicode=True, help_text='one word for title alias.', name='slug', default=uuid.uuid1)
    morpheme_type = models.CharField(max_length=1, verbose_name='형태소분석기', choices=morpheme_lists, name='morpheme_type')
    file = models.FileField(
        upload_to='files/%Y/%m',
        name='file',
        default=None,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["csv"], message="CSV 파일만 허용 가능")]
    )

    reg_date = models.DateTimeField(auto_now_add=True)

    user_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'analysis'
        db_table = 'morpheme_analysis'

    def save(self, *args, **kwargs):
        if not self.auto_increment_id:
            self.slug = slugify(self.slug, allow_unicode=True)
        else:
            self.auto_increment_id = MorphemeAnalysisModel.objects.count()
        super(MorphemeAnalysisModel, self).save(*args, **kwargs)


class Morpheme(models.Model):
    sentence = models.CharField(max_length=300)
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'morpheme'
        verbose_name_plural = 'morphemes'
        db_table = 'morpheme_morpheme'

    @staticmethod
    def morpheme_init(morpheme_type):
        print(morpheme_type)
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
        print(obj)
        for j in range(len(data_frame)):
            doc_number = str(data_frame['docNumber'][j])
            speaker_type = data_frame['speakerType'][j]
            sentence = data_frame['sentence'][j]
            yield [doc_number, speaker_type, obj.pos(sentence)]

    def __del__(self):
        print("delete object")
