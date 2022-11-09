from django import forms

from .models import *


class AddVisitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['visit_time'].empty_label = 'Дата и время не введены'

    class Meta:
        model = Visit
        fields = '__all__'
        help_texts = '2022-12-24 17:00:00'
