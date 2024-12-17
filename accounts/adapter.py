from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Check if the Google account exists, and prevent unregistered users from logging in.
        """
        user = sociallogin.user

        # Check if a user with this email exists
        if user.email and not user.is_authenticated:
            if not user.__class__.objects.filter(email=user.email).exists():
                messages.error(request, "No account associated with this Google account. Please sign up first.")
                raise Exception("No account for this email.")
