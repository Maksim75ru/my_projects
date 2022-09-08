from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
# Create your models here.


class Position(models.Model):
    name_position = models.CharField(max_length=64, default='Работник')
    description_position = models.CharField(max_length=256, default='Работает')

    def __str__(self):
        return self.name_position


class Person(models.Model):
    first_name = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    born_day = models.DateField()
    hire_day = models.DateField()
    slug = models.SlugField(default='', null=False, db_index=True)  # db_index - чтобы искать быстрее в бд
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name + '-' + self.first_name, allow_unicode=True) # allow_unicode=True позволяет принимать кириллицу
        super(Person, self).save(*args, **kwargs)

    def get_url(self):  # Создали эту функцию, чтобы в шаблоне(all_movies) прописывать не полный адрес по типу url 'name...', а эту функцию
        return reverse('employee_detail', args=[self.pk])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

