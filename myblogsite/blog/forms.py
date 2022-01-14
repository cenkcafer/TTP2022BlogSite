# A python file which is used to define and manage database for django projects
# Database are defined in this python file in django
from django import forms
# Create your forms here.
# Defining the ContactForm Table (SQL Table) to store first name, lastname, email address and
# message of a user.
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
