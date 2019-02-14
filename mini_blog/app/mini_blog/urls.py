from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tu6M5UuFseohsb/', admin.site.urls),
    path("", include("blog.urls")),
]
