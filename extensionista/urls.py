from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', view=views.home, name='home'),
    path('campanhas/', include("campaign.urls")),
    path('sobre', view=views.about, name='about'),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
