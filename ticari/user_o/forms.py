from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
class Login_form(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı" , widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}))
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput(attrs={'placeholder': 'Parola', 'class': 'form-control'}))

class Register_form(forms.Form):
    username = forms.CharField(max_length = 50,label = "Kullanıcı Adı",widget=forms.TextInput(attrs={'class': "form-control", 
                'style': 'max-width: 600px;',
                'placeholder': 'Kullanıcı Adı'}))
    email = forms.EmailField(max_length=100,label = "Email",widget=forms.EmailInput(attrs={'class': "form-control", 
                'style': 'max-width: 600px;',
                'placeholder': 'E-Posta'}))
    password = forms.CharField(max_length=20,label = "Parola",widget = forms.PasswordInput(attrs={'class': "form-control", 
                'style': 'max-width: 600px;',
                'placeholder': 'Parola'}))
    confirm = forms.CharField(max_length=20,label ="Parolayı Doğrula",widget = forms.PasswordInput(attrs={'class': "form-control", 
                'style': 'max-width: 600px;',
                'placeholder': 'Parola Doğrula'}))
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm and len(password)<6:
            raise forms.ValidationError("Parola Hatalı")
        if User.objects.filter(username = username):
            raise forms.ValidationError("Kullanıcı Adı mevcuttur")
        values = {
            "username" : username,
            "password" : password,
            "email"  : email
        }
        return values