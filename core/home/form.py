from django import forms
from froala_editor.widgets import FroalaEditor
from .models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']
        # fields = ['title', 'content', 'image']
        
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'  
            
            
    
class BlogUpdate(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content', 'image']
        
    def __init__(self, *args, **kwargs):
        super(BlogUpdate, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'  