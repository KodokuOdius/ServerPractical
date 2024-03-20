from django import forms
from .models import Task
from datetime import date


class TaskForm(forms.ModelForm):
    date_picker = forms.DateInput(attrs=dict(type='date', value=date.today))
    start_date = forms.DateField(widget=date_picker, required=True)
    end_date = forms.DateField(widget=date_picker, required=True)

    class Meta:
        model = Task
        fields = [
            'title', 'description', 'start_date',
            'end_date', 'completed', 'priority', 'assigner'
        ]

        labels = {
            'title': 'Title',
            'description': 'Description',
            'start_date': 'Start date',
            'end_date': 'End date',
            'completed': 'Completed',
            'priority': 'Priority',
            'assigner': 'Assigner'
        }
