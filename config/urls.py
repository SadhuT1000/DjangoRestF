from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lerning/", include("lerning.urls", namespace="lerning")),
    path("users/", include("users.urls", namespace="users")),

]
