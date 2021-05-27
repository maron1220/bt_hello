from django import forms


class HelloForm(forms.Form):

    data = [
        ('BUN上昇', 'BUN上昇'),
        ('BUN低下', 'BUN低下'),
        ('CRE上昇', 'CRE上昇'),
        ('CRE低下', 'CRE低下'),
        ('five', 'item5'),
    ]
    choice = forms.MultipleChoiceField(
        label='調べる項目', choices=data, widget=forms.SelectMultiple(attrs={'size': 5}))
