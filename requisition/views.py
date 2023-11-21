# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import RequisitionForm,CustomUserCreationForm
from .models import Requisition, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('requisition_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('requisition_list')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def create_requisition(request):
    if request.method == 'POST':
        form = RequisitionForm(request.POST or None, request.FILES, user=request.user)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.user = request.user
            requisition.save()
            return redirect('requisition_list')  # create a view to display requisitions
    else:
        form = RequisitionForm()

    return render(request, 'create_requisition.html', {'form': form})

@login_required
def requisition_list(request):
    if request.user.userprofile.user_type == 'normal':
        requisitions = Requisition.objects.filter(user=request.user)
    else:
        requisitions = Requisition.objects.all()

    return render(request, 'requisition_list.html', {'requisitions': requisitions})