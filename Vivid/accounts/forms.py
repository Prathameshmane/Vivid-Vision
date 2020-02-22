from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta:
        fields = ("username","email","password1","password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':"hidden"}))
    class Meta:
        model = get_user_model()
        fields = ('username', 'email','password')