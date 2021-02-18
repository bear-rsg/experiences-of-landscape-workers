from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # General app's urls
    path('', include('general.urls')),

    # Journal app's urls
    path('journal/', include('journal.urls')),

    # Account app's urls & Django's built in auth's urls
    # Share same pattern (accounts/) for consistency for user
    # Accounts app's urls must appear above Django's auth's urls to take priority
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Django admin dashboard's urls
    path('dashboard/', admin.site.urls),

    # Django PWA (progressive web app) urls
    path('', include('pwa.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
