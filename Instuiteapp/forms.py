from django import forms
from django.forms import fields, models 
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        
        labels = {
            'name':"Enter Your Name:-",
            "email":"Enter Your Email ID:-",
            "mobile_number":"Enter Your Mobile Number:-",
            "enquiry_data":"Enter Your Enquiry:-",
            "doute_triner":"Select Your Triner:-",
            "doute_course":"Selct Your Course:-",
            "date_of_post":"Enter Your Posting Date & Time :-"


        }
 