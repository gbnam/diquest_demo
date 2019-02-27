from django import forms


class SupportSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

