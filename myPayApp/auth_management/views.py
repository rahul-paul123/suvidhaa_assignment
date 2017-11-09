from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from myPayApp_admin.models import MyPayAppUser as User
from django.core.urlresolvers import reverse

@csrf_protect
def login_user(request):
    form_errors = []
    context = {}
    if request.POST:
        if (request.POST.get('username').strip() and request.POST.get(
                'password').strip()):
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username = username)
                if not user.is_staff:
                    auth_user = authenticate(username=username,
                                             password=password, request=request)
                    if auth_user:
                        login(request, auth_user)
                        if user.user_type == "Normal":
                            return redirect(reverse('accounts:user-dashboard'))
                        else:
                            return redirect(reverse(
                                'accounts:biller-dashboard'))
                    else:
                        form_errors.append("Could not be authenticated.")

            except User.DoesNotExist:
                form_errors.append("No user exists with the given username.")
        else:
            form_errors.append("Username and password cannot be empty!")

    context.update({'form_errors': form_errors})
    return render(request, 'login.html', context=context)

@csrf_protect
def logout_user(request):
    logout(request);
    return redirect(reverse('accounts:user-login'))

@csrf_protect
def user_dashboard(request):
    form_errors = []
    context = {}
    return render(request, 'user_dashboard.html', context=context)

@csrf_protect
def biller_dashboard(request):
    form_errors = []
    context = {}
    return render(request, 'biller_dashboard.html', context=context)

@csrf_protect
def change_profile(request):
    form_errors = []
    context = {}

    if request.POST:

        password = request.POST.get("password", None)
        confirm_password = request.POST.get("confirm_password", None)

        if password != confirm_password:
            form_errors.append("Password doesnot match confirmation")
        else:
            user = request.user
            user.set_password(confirm_password)
            user.save(update_fields=['password'])
            return HttpResponse("Password reset successfully")

    context.update({'form_errors': form_errors})
    return render(request, 'change_profile.html', context=context)