from django import forms
from .models import Reserve

class Res(Reserve):
    rollno = forms.CharField(help_text='MDL17CS011')

    def save(self, commit=True):
        reserve = super(Res, self).save(commit=False)
        reserve.rollno = self.cleaned_data['rollno']
        reserve.name = self.cleaned_data['name']
        reserve.email = self.cleaned_data['email']
        reserve.phone = self.cleaned_data['phone']
        reserve.date = self.cleaned_data['date']
        reserve.time = self.cleaned_data['time']

        if commit:
            user.save()
