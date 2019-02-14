from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path("<int:page_num>", views.blog, name="blog"),
    path("post/<str:post_tag>", views.get_post, name="post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)