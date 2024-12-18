from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/git-clone/api/v1/authentication/', include('authentication.api.urls')),
    path('apps/git-clone/api/v1/role/', include('role.api.urls')),
]
