from django import forms
from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError



class CreateViewForm(forms.ModelForm):

    title = forms.CharField(required=False) 
    image = forms.ImageField(required=False)
    audio = forms.FileField(required=False)

    
    class Meta:
        model = Post
        fields = ['title','content','date_posted','image','audio']

    def clean(self):
        cleaned_data = super(CreateViewForm, self).clean()

        input_field_1 = cleaned_data.get('title') 
        input_field_2 = cleaned_data.get('content')

        if input_field_1 is not None and input_field_2 is not None:
            if len(input_field_2)<3:
                
                self.add_error('content', ValidationError('The message is too short'))


class UpdateViewForm(forms.ModelForm):

    title = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    image_clear = forms.BooleanField(required=False)
    audio = forms.FileField(required=False)
    audio_clear = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = ['title','content','date_posted','image','audio']

    def clean(self):
        cleaned_data = super(UpdateViewForm, self).clean()

        input_field_1 = cleaned_data.get('title')
        input_field_2 = cleaned_data.get('content')
        input_field_3 = cleaned_data.get('date_posted')

        if input_field_1 is not None and input_field_2 is not None:
            if len(input_field_2)<3:
                self.add_error('content', ValidationError('The message is too short'))
