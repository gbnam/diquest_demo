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


class MorphemeAnalysisForm(forms.ModelForm):
    class Meta:
        model = MorphemeAnalysisModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MorphemeAnalysisForm, self).__init__(*args, **kwargs)
        self.fields['morpheme_type'].widget = forms.Select(choices=morpheme_lists, attrs={'id': '', 'required': 'required'})
        self.fields['raw_sentence'].widget = forms.TextInput(attrs={'required': 'required', 'v-on:keyup.13':'sentence_analyze'})
        self.fields['file'].required = 'required'

    def save(self, commit=True):
        morpheme = super().save(commit=False)
        print(morpheme, " : ", commit)
        if commit:
            morpheme.save()
        return morpheme
