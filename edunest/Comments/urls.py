from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create/<int:chapter_id>/', CommentCreateView.as_view(), name='create_comment'),
    path('reply/<int:chapter_id>/', ReplyCreateView.as_view(), name='reply_comment'),
    path('edit-delete/<int:id>/', CommentEditDeleteView.as_view(), name='comment-update'),
]