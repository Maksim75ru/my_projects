from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.db.models import Count, Max, Min
from .models import Person, Position
from .forms import RegistrationForm
from django.views import View
from django.views.generic import ListView
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.views.generic import DetailView
# Create your views here.


def show_all_employees(request):
    employees = Person.objects.order_by('first_name')
    agg = employees.aggregate(Count('id'), Max('born_day'), Min('born_day'))
    old_employee = Person.objects.order_by('born_day')[0]
    young_employee = Person.objects.order_by('-born_day')[0]

    today_year = date.today().year

    max_age_employee = agg.get('born_day__min').year
    old_age_employee = today_year - max_age_employee

    min_age_employee = agg.get('born_day__max').year
    young_age_employee = today_year - min_age_employee

    return render(request, 'rst_birthday_app/employees.html', {
        'employees': employees,
        'agg': agg,
        'old_employee': old_employee,
        'young_employee': young_employee,
        'old_age_employee': old_age_employee,
        'young_age_employee': young_age_employee,
    })


class ShowOneEmployee(DetailView):  # Отображает детальную информацию о работнике по pk
    template_name = 'rst_birthday_app/one_employee.html'
    model = Person
    context_object_name = 'employee'





class AddNewEmployee(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'rst_birthday_app/registration_page.html', context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/done')
            return render(request, 'rst_birthday_app/registration_page.html', context={'form': form})


def done(request):
    return render(request, 'rst_birthday_app/done.html')
