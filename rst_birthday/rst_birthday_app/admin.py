from django.contrib import admin
from .models import Person
from datetime import date
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['first_name', 'last_name', 'name_position', 'born_day', 'hire_day', 'time_work', 'age_employee']
    list_editable = ['name_position', 'born_day', 'hire_day']
    ordering = ['-born_day']
    list_per_page = 10
    search_fields = ['last_name__startswith']
    list_filter = ['name_position']

    @admin.display(description='Время работы в компании')
    def time_work(self, data: Person):
        today = date.today()
        if (today.year - data.hire_day.year) < 2:
            return 'Сотрудник работает менее 2 лет'
        return 'Сотрудник работает более 2 лет'

    @admin.display(description='Возраст сотрудника')
    def age_employee(self, data: Person):
        today = date.today()
        return today.year - data.born_day.year


admin.site.register(Person, PersonAdmin)
