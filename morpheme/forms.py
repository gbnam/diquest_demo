from django import forms


class SentenceForm(forms.Form):
    morpheme_choices = (
        ('', u'선택'),
        ('mecab', u'mecab'),
        ('jiana', u'jiana')
    )

    morpheme_type = forms.ChoiceField(choices=morpheme_choices, label='형태소 분석기')
    raw_sentence = forms.CharField(max_length=300, label='원문정보',
                                   widget=forms.TextInput(attrs={'onkeypress': 'sentence_analyze();'}))
    parsed_sentence = forms.CharField(max_length=300, label='변환정보 ',
                                      widget=forms.TextInput(attrs={'readonly': 'readonly'}))
