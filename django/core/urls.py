from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # General app's urls
    path('', include('general.urls')),

    # Journal app's urls
    path('api/', include('journal.urls')),

    # Django admin dashboard's urls
    path('dashboard/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
