from registration.forms import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def resetuserinfo(request, user):
    print(user)
    print(User.objects.all())
    userinfo = get_object_or_404(User, username=user)
    print(userinfo.first_name)
    print(userinfo.last_name)
    print(userinfo.email)
    print(userinfo)
    userinfo = get_object_or_404(User, username=request.POST['user.username'])
    print(userinfo)
    userinfo.first_name = request.POST.get('first_name')
    print(userinfo.first_name)
    userinfo.last_name = request.POST.get('last_name')
    print(userinfo.last_name)
    userinfo.email = request.post.get('email')
    print(userinfo.email)
    userinfo.save()
    return HttpResponseRedirect(reverse('profile'))
