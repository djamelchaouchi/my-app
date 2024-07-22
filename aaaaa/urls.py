from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('admin/', admin.site.urls),
]

# handler404 = 'pages.views.error_404_view'  404 page
