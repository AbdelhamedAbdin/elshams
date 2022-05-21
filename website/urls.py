from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
from django.conf.urls.static import static

from website import settings as web_base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.home.urls")),
    path('contact-us/', include("apps.contact.urls")),
    path('about-us/', include("apps.about_us.urls")),
    path('admission/', include("apps.admission.urls")),
    path('gallery/', include("apps.gallery.urls")),
    path('events/', include("apps.events.urls")),
]

urlpatterns += static(web_base.base.STATIC_URL, document_root=web_base.base.STATIC_ROOT)
urlpatterns += static(web_base.base.MEDIA_URL, document_root=web_base.base.MEDIA_ROOT)
