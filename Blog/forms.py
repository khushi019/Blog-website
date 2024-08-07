from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import AuthenticationForm


class BlogForm(forms.ModelForm):
    # content=forms.CharField(widget=forms.Textarea(attrs={'rows':15,'cols':23}))
    class Meta:
        model=Blog
        fields=['title','content']

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email','password1','password2']:
            self.fields[fieldname].help_text = None

class EditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email',]:
            self.fields[fieldname].help_text = None
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
        
class ShareForm(forms.Form):
    to = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea, label='Why are you sharing this blog?')  



class CaptchaForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)