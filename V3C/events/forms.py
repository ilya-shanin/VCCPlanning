from django import forms
from django.core.exceptions import ValidationError

from events.models import Conference

class EventCreationForm(forms.Form):
    class Meta:
        model = Conference
        fields = ['name', 'start_time', 'end_time', 'notes', 'con_reference', 'con_pass', 'is_active']

    def clean_end_time(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if end_time <= start_time:
            raise forms.ValidationError("Дата окончания события должна быть позже даты его начала")
        return super(EventCreationForm, self).clean()

    def save(self, commit=True):
        event = super().save(commit=False)
        if commit:
            event.save()
        return event

class EventChangeForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'start_time', 'end_time', 'notes', 'con_reference', 'con_pass', 'is_active']

        def clean_end_time(self):
            start_time = self.cleaned_data.get('start_time')
            end_time = self.cleaned_data.get('end_time')
            if end_time <= start_time:
                raise forms.ValidationError("Дата окончания события должна быть позже даты его начала")
            return super(EventCreationForm, self).clean()