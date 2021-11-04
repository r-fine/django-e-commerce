from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login

from .models import LocalUser


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            # if user exists, connect the account to the existing account and login
            customer = LocalUser.objects.get(email=user.email)
            sociallogin.state['process'] = 'connect'
            perform_login(request, customer, 'none')
        except LocalUser.DoesNotExist:
            pass


"""
references:
https://stackoverflow.com/questions/28897220/django-allauth-social-account-connect-to-existing-account-on-login
https://github.com/pennersr/django-allauth/issues/418#issuecomment-38391830
"""
