from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("projects.urls", namespace="projects")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("api/", include("api.urls")),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="reset/reset_password.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="reset/reset_password_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",  # by default
        auth_views.PasswordResetConfirmView.as_view(
            template_name="reset/reset_password_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",  # by default
        auth_views.PasswordResetCompleteView.as_view(
            template_name="reset/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
