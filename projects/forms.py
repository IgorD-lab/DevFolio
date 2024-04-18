from django.forms import ModelForm
from django import forms 
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
        def __init__(self, *args, **kwarg):
            super(ProjectForm, self).__init__(*args, **kwarg)
        
            for name, field in self.fields.items():
                field.widget.attributes.update({'class':'input'})
        
        # def __init__(self, *args, **kwarg):
        #     super(ProjectForm, self).__init__(*args, **kwarg)
            
        #     self.fields['title'].widget.attrs.update({'class':'input',  })