from django import forms
from .models import Project
from django.forms import widgets

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        # fields='__all__'
        # labels={'':''}
        exclude=['owner']

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'}) #ovako smo polju title promijenili klasu
        self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add description'})
        self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add demo link'})
        self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add source link'})

