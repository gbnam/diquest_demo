from django import forms
from .models import *


class SentenceForm(forms.Form):
    morpheme_choices = (
        ('', u'선택'),
        ('mecab', u'mecab'),
        ('jiana', u'jiana'),
        ('kkma', u'kkma'),
        ('komoran', u'komoran'),
        ('okt', u'okt'),
        ('hannanum', u'hannanum')
    )

    morpheme_type = forms.ChoiceField(choices=morpheme_choices, label='형태소 분석기')
    raw_sentence = forms.CharField(max_length=300, label='원문정보')
    parsed_sentence = forms.CharField(max_length=300, label='변환정보 ',
                                      widget=forms.TextInput(attrs={'readonly': 'readonly'}))


class FileForm(forms.ModelForm):
    class Meta:
        model = CsvDocument
        fields = ['file_morpheme_type','file']

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = True


class MorphemeForm(SentenceForm, FileForm):
    pass
