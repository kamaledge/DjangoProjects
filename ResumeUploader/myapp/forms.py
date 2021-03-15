from django.forms import fields, widgets
from .models import Resume
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    help_texts = {'password1': None}

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'is_staff']
        labels = {'email': 'Email', 'is_staff':'Recruiter'}
        help_texts = {
            'is_staff': None,
            'username': None,
        }
        
 


GENDER_CHOICES = [
    ('M','Male'),
    ('F', 'Female')
]

JOB_CITY_CHOICE = (
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Pune','Pune'),
    ('Bangalore','Bangalore'),
    ('Hyderabad','Hyderabad'),
    ('Chennai','Chennai'),
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(label='Preffered Job Location', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        exclude = ['id']

        labels = {'name': 'Full Name', 
        'dob': 'Date of Birth',
        'location': 'Address',
        'mobile': 'Contact No',
        'pin': 'PIN Code',
        'my_file': 'Document',
        'prfile_image': 'Profile Image'
        }


        widgets = {
            # field.name : forms.TextInput(attrs={'class': 'form-control'}) for field in Resume._meta.get_fields() if field.name in ('name', 'locality','city')
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
            'dob': forms.widgets.DateInput(attrs={'class': 'form-control', 'id':'datepicker'}),
            'locality': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'city': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.widgets.Select(attrs={'class': 'form-control'}),
            'mobile': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.widgets.EmailInput(attrs={'class': 'form-control'}),
        }