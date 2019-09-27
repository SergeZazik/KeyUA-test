from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Entry


class EntryModelForm(forms.ModelForm):
    date = forms.DateField(widget=DatePicker(
        attrs={
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }
    ))

    class Meta:
        model = Entry
        fields = ['date', 'distance', 'duration']


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DatePicker(
        attrs={
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }
    ))
    end_date = forms.DateField(widget=DatePicker(
        attrs={
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }
    ))
