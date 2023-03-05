from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        # Needs two values: define which model from models file import it and which fields are given
        # U can give a list with each field in 'fields' variable or str "__all__" for all fields
        model = Task
        fields = "__all__"