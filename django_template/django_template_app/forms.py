from django import forms
from .models import ContactInfo, PersonalInfo, UserProfile, Request



class PersonalInfoForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = (
            'first_name',
            'last_name',
            'company'
        )


class ContactInfoForm(forms.ModelForm):

    class Meta:
        model = ContactInfo
        fields = (
            'email',
            'phone',
            'address',
            'suite',
            'city',
            'state',
            'zip_code'
        )

class UserProfileForm(forms.ModelForm):

    personal_info = PersonalInfoForm(prefix="personal")
    contact_info = ContactInfoForm(prefix="contact")

    class Meta:
        model = UserProfile
        fields = ()

    def __init__(self, *args, **kwargs):
        contact_data = kwargs.pop('contact_data', None)
        personal_data = kwargs.pop('personal_data', None)
        
        super().__init__(*args, **kwargs)

        self.contact_form = ContactInfoForm(contact_data, prefix="contact")
        self.personal_form = PersonalInfoForm(personal_data, prefix="personal")

    def is_valid(self):
        return super().is_valid() and self.contact_form.is_valid() and self.personal_form.is_valid()

    def save(self, commit=False):
        user = super().save(commit=False)

        contact_info = self.contact_form.save(commit=commit)
        personal_info = self.personal_form.save(commit=commit)

        user.contact = contact_info
        user.personal = personal_info
    
    


class RequestForm(forms.ModelForm):


    class Meta:
        model = Request
        fields = [
            'project_name',
            'project_description',
            'user'
        ]

        
        
