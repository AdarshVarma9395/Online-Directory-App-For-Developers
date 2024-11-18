from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Skill, Message



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        
        labels = {
            'first_name':'Full Name',  #here it only changed label not the acctual field name
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        placeholders = {
        'username': 'Enter your username',
        'email': 'Enter your email address',
        'first_name': 'Enter your First and Last Name',
        'password1': 'Enter password',
        'password2': 'Confirm password',
        }

        for name, field in self.fields.items():    
            field.widget.attrs.update({'class': 'input'})

            if name in placeholders:
                field.widget.attrs.update({'placeholder': placeholders[name]})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        placeholders = {
        'name': 'Enter your full name',
        'email': 'Enter your email address',
        'username': 'Choose a username',
        'location': 'Enter your location',
        'bio': 'Tell us about yourself',
        'short_intro': 'Write a short introduction about you',
        'profile_image': 'Upload your profile picture',
        'social_github': 'Enter your GitHub profile URL',
        'social_linkedin': 'Enter your LinkedIn profile URL',
        'social_twitter': 'Enter your Twitter profile URL',
        'social_youtube': 'Enter your YouTube channel URL',
        'social_website': 'Enter your personal website URL'
        }

        for name, field in self.fields.items():    
            field.widget.attrs.update({'class': 'input'})

            if name in placeholders:
                field.widget.attrs.update({'placeholder': placeholders[name]})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        
        placeholders = {
        'name': 'Enter your Skill',
        'description': 'Enter Description',
        }

        for name, field in self.fields.items():    
            field.widget.attrs.update({'class': 'input'})

            if name in placeholders:
                field.widget.attrs.update({'placeholder': placeholders[name]})



class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

        labels = {
            'body':'Enter Text'
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        
        placeholders = {
        'name': 'Enter your Full Name',
        'email': 'Enter your Email',
        'subject':'Enter your Subject',
        'body':'Enter Your Message'
        }

        for name, field in self.fields.items():    
            field.widget.attrs.update({'class': 'input'})

            if name in placeholders:
                field.widget.attrs.update({'placeholder': placeholders[name]})