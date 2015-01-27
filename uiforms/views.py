from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import UiForm


def show_form(request, form_obj, read_only=False):
    """Given a form objects renders it on the UI."""
    return render_to_response('preview.html', RequestContext(request, {
        'obj': form_obj,
        'read_only': read_only,
    }))


def render_form(request, form_id):
    """Given a form id renders the form.

    If user is not logged in shows only a read only version of the form.
    """
    obj = get_object_or_404(UiForm, pk=form_id)
    print request.user.is_authenticated()
    return show_form(
        request, obj, read_only=not request.user.is_authenticated())
