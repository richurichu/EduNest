from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

router.register(r'discussions-replies', DiscussionRepliesViewSet)




urlpatterns = [
    path('', include(router.urls)),
  
    path('create/<int:chapter_id>/', CommentCreateView.as_view(), name='create_comment'),
    path('reply/<int:chapter_id>/', ReplyCreateView.as_view(), name='reply_comment'),
    path('edit-delete/<int:id>/', CommentEditDeleteView.as_view(), name='comment-update'),
    path('discussion/', QuestionListCreateView.as_view(), name='discussion'),
    path('response-create/<int:Question_id>/', DiscussionResponseCreateView.as_view(), name='create_response'),
    path('nested-response-create/<int:Question_id>/', DiscussionNestedReplyCreateView.as_view(), name='create_nested_response'),
    
     path('discussion-edit-delete/<int:id>/', DiscussionEditDeleteView.as_view(), name='discussion-update'),
]