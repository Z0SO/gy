from django.contrib import admin
from django.urls import path
from django.urls import include

from hc import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('hc.urls'))
]

