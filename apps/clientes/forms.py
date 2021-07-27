from django.forms import ModelForm
from . models import Person
from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['frist_name', 'last_name',
                  'age', 'salary', 'bio', 'photo', 'doc']
