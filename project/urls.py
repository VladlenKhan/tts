from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('set_language/', set_language, name='set_language'),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
