from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from models import BetaInviteRequest


class BetaInviteRequestForm(forms.ModelForm):
    """
    """

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            user = User.objects.get(email=data)
            raise forms.ValidationError(_(u'An user with this email already exists.'))
        except User.DoesNotExist:
            pass
        return data

    class Meta:
        model = BetaInviteRequest
