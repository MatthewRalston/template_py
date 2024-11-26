from django import forms
from .models import User, Project


class UserForm(forms.ModelForm):
    """
    Form for users
    """

    class Meta:
        model = User
        fields = [
            'personal.first_name',
            'personal.last_name',
            'personal.company',
            'contact.email',
            'contact.phone',
            'contact.address',
            'contact.suite',
            'contact.city',
            'contact.state',
            'contact.zip_code'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)

        contact_info, _ = User.ContactInfo.objects.get_or_create(
            email=self.cleaned_data['contact.email'],
            phone=self.cleaned_data['contact.phone'],
            address=self.cleaned_data['contact.address'],
            suite=self.cleaned_data['contact.suite'],
            city=self.cleaned_data['contact.city'],
            state=self.cleaned_data['contact.state'],
            zip_code=self.cleaned_data['contact.zip_code']
            
        )

        personal_info, _ = User.PersonalInfo.objects.get_or_create(
            first_name=self.cleaned_data['personal.first_name'],
            last_name=self.cleaned_data['personal.last_name'],
            company=self.cleaned_data['personal.company']
        )
        
        user.contact = contact_info
        user.personal = personal_info


        if commit:
            user.save()

        return user



class ProjectForm(forms.ModelForm):


    class Meta:
        model = Project
        fields = [
            'project_name',
            'project_description',
            'user'
        ]

        
        
