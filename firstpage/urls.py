from django.contrib import admin
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
]
handler404 = 'firstpage.views.handler404'