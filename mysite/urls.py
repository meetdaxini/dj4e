import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView


# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('hello/', include('hello.urls'), name='hello' ),
    path('accounts/', include('django.contrib.auth.urls')),  # Add
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('ads/', include('ads.urls')),

]

urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]