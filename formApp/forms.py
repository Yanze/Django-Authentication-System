from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label='Your Fullname', max_length=100)
