from django.forms import ModelForm
from django import forms
from .models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['title', 'featured_image', 'description','demo_link', 'source_link']
        exclude = ['vote_total', 'vote_ratio', 'owner']

        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        placeholders = {
        'title': 'Enter the project title',
        'featured_image': 'Upload an image',
        'description': 'Provide a brief description',
        'demo_link': 'Enter the demo URL',
        'source_link': 'Enter the source code URL',
        }

        for name, field in self.fields.items():    # using for-loop to change class of the field 
            field.widget.attrs.update({'class': 'input'})

            if name in placeholders:
                field.widget.attrs.update({'placeholder': placeholders[name]})


        # self.fields['title'].widget.attrs.update({'class': 'input'}) ---->we can also change the css class one by one 
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder':'enter discription'})
        #                                                                                              -->can also use placeholder