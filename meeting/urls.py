from django.contrib import admin
from django.urls import path, include
from main.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('app/', include('app.urls')),
    path('accounts/', include('accounts.urls')),
]

from django.conf import settings
from django.conf.urls import include, url
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] 