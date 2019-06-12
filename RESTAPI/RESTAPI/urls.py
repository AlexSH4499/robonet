
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import  format_suffix_patterns


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('roboIF.urls')),
    path(r'api-auth/', include('rest_framework.urls'))
]

#urlpatterns = format_suffix_patterns(urlpatterns)
