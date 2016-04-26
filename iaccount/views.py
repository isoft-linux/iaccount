from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User

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
