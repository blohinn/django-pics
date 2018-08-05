from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import ProfileForm


def profile(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profileapp/profile.html', {
        'user': user
    })


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            # TODO validating uploaded photo
            form.save()
            return redirect(reverse('profileapp:edit'))
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profileapp/edit_profile.html', {
        'user': request.user,
        'form': form
    })
