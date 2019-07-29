from django import forms
from .models import EBook


class EBookForm(forms.ModelForm):
	class Meta:
		model = EBook
		exclude = ('name',)