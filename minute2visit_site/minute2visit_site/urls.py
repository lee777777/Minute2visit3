
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from first_page.views import custom_404, custom_500

urlpatterns = [
    path("", include("first_page.urls")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'first_page.views.custom_404'
# handler500 = 'first_page.views.custom_500'