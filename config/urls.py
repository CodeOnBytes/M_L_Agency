from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# THE FIX: This tells Django to serve files from STATIC_ROOT when accessed via STATIC_URL
if settings.DEBUG or True:  # Forced to true so WhiteNoise catches routing on Vercel
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
