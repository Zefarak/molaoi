from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password"]

    def save(self, commit=True):
        user =super(MyRegistrationForm,self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user

