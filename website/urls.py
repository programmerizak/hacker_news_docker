
from django.contrib import admin
from django.urls import path, include


### IMPORTED FOR CONFIGURATION PURPOSE FOR STATIC AND MEDIA FILES
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap


admin.site.site_header = "HACKERS NEWS V2.0 ADMIN"
admin.site.site_title = "HACKERS NEWS V2.0 ADMIN PORTAL"
admin.site.index_title = "WELCOME TO HACKERS NEW V2.0 PORTAL"

urlpatterns = [
    path('secret-page/', admin.site.urls),
    path('', include('items.urls', namespace='items')),
    path('api/', include('api.urls', namespace='api')),
    path('auth/', include('allauth.urls')),
]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
