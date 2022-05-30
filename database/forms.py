from django import forms
from .models import Devices, Hotel


class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'hotel_Main_Img']


class DataForm(forms.Form):

	name = forms.CharField(max_length=50, label='Your Name')
	age = forms.IntegerField(label='Your Age')



# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     source = forms.CharField(       # A hidden input for internal use
#         max_length=50,              # tell from which page the user sent the message
#         widget=forms.HiddenInput()
#     )

#     def clean(self):
#         cleaned_data = super(ContactForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass

class DeviceConfigForm(forms.ModelForm):

    class Meta:
        model = Devices
        fields = ['ssid', 'password', 'device_ip', 'broker_ip', 'gateway', 'subnet', 'port', 'mqtt_username', 'mqtt_password']