from bokeh.embed import server_document

from django.http import HttpRequest
from django.shortcuts import render


def example(request: HttpRequest) -> object:
    """ Render the autoloaded bokeh app.

    The example view is used by all three different bokeh apps.
    It requires to set up the autoload on specified routes in the main settings.py

    Args:
        request:

    Returns:
        object:

    """
    script = server_document(request.build_absolute_uri())
    return render(request, "visualization_bokeh/embed.html", dict(script=script))
