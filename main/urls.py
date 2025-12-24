from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("comments/<int:id>", views.comment_view, name="comment_section"),
    path("register", views.register_view, name="register_page"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", LogoutView.as_view(next_page="main_page"), name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile_view, name="edit_profile"),
    path("profile/<int:user_id>/", views.other_profile_view, name="other_profile"),
    path("posts/create/", views.post_cr_view, name="post_cr")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)