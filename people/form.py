from .models import Person
from django.forms import ModelForm

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["name", "last_name","years_old","birth","email","nickname","obervation"]