"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import visualization_bokeh.bk_app as bokeh_app  # noqa
import visualization_bokeh.bk_app_ipywidgets as ipyaggrid_app  # noqa
#import visualization_bokeh.pn_app as panel_app  # noqa

from bokeh.server.django import autoload, static_extensions
from django.apps import apps
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

pn_app_config = apps.get_app_config('bokeh.server.django')

# Register django apps
urlpatterns = [
    path('', include('home.urls')),
    path('charts/', include('visualization_chartjs.urls')),
    path('django_formset_vuejs/', include('django_formset_vuejs.urls')),
    path('api/', include('api.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('visualization_dash/', include('visualization_dash.urls')),
    path('visualization_bokeh/', include('visualization_bokeh.urls')),
    path('messaging/', include('messaging.urls')),
    url('^django_plotly_dash/', include('django_plotly_dash.urls')),
   # url(r'^docs/', include('sphinxdoc.urls')),
    path('chat/', include('chat.urls')),
    path('crud/', include('crud.urls')),
    path("unicorn/", include("django_unicorn.urls"))

]

# Register bokeh apps here!
bokeh_apps = [
    autoload("visualization_bokeh", bokeh_app.app),
    autoload("visualization_bokeh/ipywidget", ipyaggrid_app.app),
  #  autoload("visualization_bokeh/panel", panel_app.app)
]

urlpatterns += static_extensions()
urlpatterns += staticfiles_urlpatterns()
