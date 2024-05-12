from django.forms import ModelForm
from django import forms 
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link']
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
        def __init__(self, *args, **kwarg):
            super(ProjectForm, self).__init__(*args, **kwarg)
        
            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
        
        # def __init__(self, *args, **kwarg):
        #     super(ProjectForm, self).__init__(*args, **kwarg)
            
        #     self.fields['title'].widget.attrs.update({'class':'input',  })
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']
    
        labels = {
            'value': 'Place your vote',
            'boy': 'Add a comment with your vote'
        }
        
    def __init__(self, *args, **kwarg):
            super(ReviewForm, self).__init__(*args, **kwarg)
        
            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})