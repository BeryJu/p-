"""p2 Root URLs"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from django.views.generic import RedirectView

from p2.ui.views.errors import ServerErrorView

admin.site.index_title = 'p2 Admin'
admin.site.site_title = 'p2'
admin.site.login = RedirectView.as_view(
    pattern_name='p2_ui:index', permanent=True, query_string=True)

handler500 = ServerErrorView.as_view()

# S3 URLs get routed via middleware
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='p2_ui:index')),
    path('_/admin/', admin.site.urls),
    path('_/api/', include('p2.api.urls', namespace='p2_api')),
    path('_/ui/', include('p2.ui.urls', namespace='p2_ui')),
    path('_/oidc/', include('mozilla_django_oidc.urls')),
    path('_/auth/password/', views.PasswordChangeView.as_view(), name='auth_password'),
    path('_/auth/login/', views.LoginView.as_view(), name='auth_login'),
    path('_/auth/logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('', include('p2.s3.urls', namespace='p2_s3')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('_/debug/', include(debug_toolbar.urls)),
    ] + urlpatterns
