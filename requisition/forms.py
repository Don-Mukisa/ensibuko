from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Requisition,UserProfile
from django.contrib.auth.models import User


class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        
        fields = ['title', 'description', 'upload_file', 'amount', 'approved']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)  # Add any additional fields you want for signup
