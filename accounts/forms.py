from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control  ','id':'pass'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control   '}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email',)
        widgets = { 
                'username':forms.TextInput(attrs={'class':'form-control   '}),
                'first_name':forms.TextInput(attrs={'class':'form-control   '}),
                'last_name':forms.TextInput(attrs={'class':'form-control   '}),
                'email':forms.TextInput(attrs={'class':'form-control  '}),}
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'pass'}))
    
class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('first_name', 'last_name','email')
            widgets ={
                'first_name':forms.TextInput(attrs={'class':'form-control  '}),
                'last_name':forms.TextInput(attrs={'class':'form-control  '}),
                'email':forms.TextInput(attrs={'class':'form-control  '}),
                
            }
