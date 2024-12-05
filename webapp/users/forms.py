from django import forms
from ..models import Usuario

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'phone', 'address', 'role']
        widgets = {
            'password': forms.PasswordInput,
        }

    def save(self, commit=True, role=None):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if role:
            user.role = role
        if commit:
            user.save()
        return user
    