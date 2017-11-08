import json

from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from .forms import (CustomAuthForm, UserProfileForm, BillerProfileForm)
from .models import UserProfile

def login_admin(request):
    form = CustomAuthForm()
    errors = []
    redirect_url = request.GET.get('next', None)
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        try:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_staff:
                    login(request, user)
                    if redirect_url:
                        return redirect(redirect_url)
                    return redirect(reverse('app-admin:dashboard'))
                else:
                    errors.append('Only admin can login.')
            else:
                errors.append('Couldn\'t be authenticated.')
        except:
            errors.append('Something went wrong. Please try later.')
    context = {'form':form, 'errors':errors}
    return render(request, 'app_admin/login.html', context=context)

def logout_admin(request):
    logout(request);
    return redirect(reverse('app-admin:login'))

@login_required(login_url='app-admin:login')
def dashboard(request):
    return render(request, 'app_admin/dashboard.html')

@login_required(login_url='app-admin:login')
def register_user(request):

    form = UserProfileForm()
    errors = []
    redirect_url = request.GET.get('next', None)
    if request.POST:
        form = UserProfileForm(request.POST)
        if form.is_valid():
            password = request.POST.get("password", None)
            if password:
                user_profile = form.save()
                user_profile.set_password(password)
                user_profile.save(update_fields=['password'])
            else:
                return HttpResponse('Please enter a password.')
            if user_profile:
                return HttpResponse('User creation successfull.')
            else:
                return HttpResponse("User creation failed.")
    context = {'form':form, 'errors':errors}
    return render(request, 'app_admin/register_user.html', context=context)

@login_required(login_url='app-admin:login')
def register_biller(request):

    form = BillerProfileForm()
    errors = []
    redirect_url = request.GET.get('next', None)
    if request.POST:
        form = BillerProfileForm(request.POST)
        if form.is_valid():
            password = request.POST.get("password", None)
            print(password)
            if password:
                biller_profile = form.save()
                biller_profile.set_password(password)
                biller_profile.user_type = "Biller"
                biller_profile.save(update_fields=['password','user_type'])
            else:
                return HttpResponse('Please enter a password.')
            if biller_profile:
                return HttpResponse('Biller creation successfull.')
            else:
                return HttpResponse("Biller creation failed.")
    context = {'form':form, 'errors':errors}
    return render(request, 'app_admin/register_biller.html', context=context)
