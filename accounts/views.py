from allauth import account
from django.shortcuts import render


def account_dashboard(request):

    return render(request, 'account/dashboard.html', {})
