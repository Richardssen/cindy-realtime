import re

from django.conf import settings
from django.shortcuts import HttpResponse, redirect, render, render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie

from sui_hei.models import *

I18N_PATTERN_REGEX = re.compile(r'^/(en|ja)')
DEBUG = settings.DEBUG


@ensure_csrf_cookie
def main(request, *args, **kwargs):
    if DEBUG:
        return render(request, "index_debug.html")
    return render(request, "index_prod.html")


def serviceWorker(request, *args, **kwargs):
    return render_to_response("sw.js", content_type="text/javascript")


def remove_i18n_pattern(request, *args, **kwargs):
    return redirect(I18N_PATTERN_REGEX.sub("", request.path))


def event(request, eventId, *args, **kwargs):
    ev = Event.objects.get(pk=eventId)
    return HttpResponse(ev.page_src) if ev.page_src else redirect('/')
