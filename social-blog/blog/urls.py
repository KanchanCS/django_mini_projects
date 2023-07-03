from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    # Home page
    path("", views.home, name="post"),
    path("post/detail/<int:id>", views.post_detail, name="post-detail"),
    path("post/create/", views.create_post, name="create-post"),
    path("person/<int:id>", views.view_person, name="view-person"),
    path("follow-<int:person_id>/", views.follow, name="follow"),
    path("unfollow-<int:person_id>/", views.unfollow, name="unfollow"),
    path("like-<int:post_id>/", views.like, name="like"),
    path("unlike-<int:post_id>/", views.unlike, name="unlike"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
