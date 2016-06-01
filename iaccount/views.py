from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.module_loading import import_string
from django.views.decorators.debug import sensitive_post_parameters

def profilereset(request):
    change_flag = False
    user_name = request.POST['username']
    user_first_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_email = request.POST['email']
    user_password = request.POST['password']
    userinfo = get_object_or_404(User, username=user_name)
    if not userinfo:
        errors = "user don't exsit"
        return HttpResponseRedirect(reverse('profile'))
    try:
        password_validation.validate_password(user_password, user_name)
    except ValidationError as error:
        errors = "the password don't match"
        return HttpResponseRedirect(reverse('profile'))
    if userinfo.email != user_email:
        change_flag = True
        userinfo.email = user_email
    if userinfo.first_name != user_first_name:
        change_flag = True
        userinfo.email = user_first_name
    if userinfo.last_name != user_last_name:
        change_flag = True
        userinfo.email = user_last_name
    if change_flag:
        userinfo.save()

    return HttpResponseRedirect(reverse('profile'))

REGISTRATION_FORM_PATH = getattr(settings, 'REGISTRATION_FORM',
                                 'registration.forms.RegistrationForm')
REGISTRATION_FORM = import_string(REGISTRATION_FORM_PATH)

class RegistrationView(FormView):
    """
    Base class for user registration views.

    """
    disallowed_url = 'registration_disallowed'
    form_class = REGISTRATION_FORM
    http_method_names = ['get', 'post', 'head', 'options', 'trace']
    success_url = None
    template_name = 'registration/registration_form.html'

    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    def dispatch(self, request, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.

        """
        if not self.registration_allowed():
            return redirect(self.disallowed_url)
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if not form.is_valid():
            return redirect(self.disallowed_url)
        new_user = self.register(form)
        success_url = self.get_success_url(new_user)

        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
        except ValueError:
            return redirect(success_url)
        else:
            return redirect(to, *args, **kwargs)

    def registration_allowed(self):
        """
        Override this to enable/disable user registration, either
        globally or on a per-request basis.

        """
        return True

    def register(self, form):
        """
        Implement user-registration logic here.

        """
        raise NotImplementedError

    def get_success_url(self, user=None):
        """
        Use the new user when constructing success_url.

        """
        return super(RegistrationView, self).get_success_url()
