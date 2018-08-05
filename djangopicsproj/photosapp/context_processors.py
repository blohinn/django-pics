from .forms import PhotoForm


def upload_photo_form(request):
    form = PhotoForm()
    return {'upload_photo_form': form}
