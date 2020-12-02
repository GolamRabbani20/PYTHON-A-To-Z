from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path('',include("cale.urls")),
    path('',include("Lily.urls")),
    path('admin/', admin.site.urls),
]
