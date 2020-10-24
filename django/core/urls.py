from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # Client web app's urls
    path('', include('clientweb.urls')),

    # API app's urls
    path('api/', include('api.urls')),

    # Django admin dashboard's urls
    path('dashboard/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
