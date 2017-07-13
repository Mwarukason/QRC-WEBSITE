from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from qrcblog.views import post_create, post_detail,post_list,post_update,post_delete
#importing app views
#from qrcblog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #include all urls of app qrcblog
    #namespace make easier to have multiple same name dif apps
    #used for set of urls
    url(r'^', include("qrcblog.urls", namespace="qrcblog")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
