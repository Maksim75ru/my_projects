from django import forms
from .models import Person, Position
from django.forms import ModelForm, Textarea, CharField, Select
from django.forms import inlineformset_factory

# class RegistrationForm(forms.Form):
#     first_name = forms.CharField(max_length=20, min_length=2, label='Имя', error_messages={
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов',
#         'required': 'Укажите хотя бы 1 символ',
#     })
#     last_name = forms.CharField(max_length=30, min_length=2, label='Фамилия', error_messages={
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов',
#         'required': 'Укажите хотя бы 1 символ',
#     })
#     born_day = forms.DateField(label='Дата рождения в формате гггг-мм-дд')
#     hire_day = forms.DateField(label='Дата трудоустройства в формате гггг-мм-дд')
#     position = forms.CharField(max_length=30, label='Должность')


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Person
        # fields = '__all__'
        exclude = ['slug']

        # widgets = {   # Нужно переопределить чтобы данные вносились в две таблицы и была связь между ними
        #     'position': Textarea()
        # }

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'born_day': 'Дата рождения в формате гггг-мм-дд',
            'hire_day': 'Дата трудоустройства в формате гггг-мм-дд',
            'position': 'Должность',
        }
        error_messages = {
            'first_name': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Укажите хотя бы 2 символ',
            },
            'last_name': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Укажите хотя бы 2 символ',
            },
        }


