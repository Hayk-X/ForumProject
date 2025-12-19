from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("comments/<int:id>", views.comment_view, name="comment_section")
]