from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import PhotoForm


@login_required
@require_http_methods(["POST"])
def upload_photo(request):
    form = PhotoForm(request.POST)
    if form.is_valid():
        # TODO validating uploaded photo
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'Photo uploaded.')
        return redirect(reverse('photosapp:photo_feed'))
    messages.add_message(request, messages.ERROR, 'Error uploading photo.')
    return redirect(reverse('photosapp:photo_feed'))


@login_required
def photo_feed(request):
    return render(request, 'photosapp/photo_feed.html')
