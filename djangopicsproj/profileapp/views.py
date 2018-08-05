from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import ProfileForm
from photosapp.models import Photo


def profile(request, username):
    user = get_object_or_404(User, username=username)
    photos = Photo.objects.filter(owner=user).all()

    return render(request, 'profileapp/profile.html', {
        'user': user,
        'photos': photos
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
