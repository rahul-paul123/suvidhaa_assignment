from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse

@login_required
def dispatch(request):
    user = request.user
    if user.is_staff:
        return redirect(reverse('app-admin:dashboard'))
    else:
        return render(request, 'login.html', context={})