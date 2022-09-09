from django import forms
from .models import Person


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
            'name_position': 'Должность',
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
