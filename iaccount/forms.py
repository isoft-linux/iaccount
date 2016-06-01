"""
Forms and validation code for user registration.

Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.

"""
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from registration.users import UserModel
from captcha.fields import CaptchaField

User = UserModel()

class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    username = forms.CharField(max_length=30)
    email = forms.EmailField(label=_("E-mail"))
    first_name = forms.CharField(max_length=30, label=_("first name"))
    last_name = forms.CharField(max_length=30, label=_("last name"))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "captcha")
