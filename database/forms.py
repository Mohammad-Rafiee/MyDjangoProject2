from django import forms
from .models import Hotel


class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'hotel_Main_Img']


class DataForm(forms.Form):

	name = forms.CharField(max_length=50, label='Your Name')
	age = forms.IntegerField(label='Your Age')