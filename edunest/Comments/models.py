from django.db import models
from authentification.models import *
from Courses.models import *

class Comment(models.Model):
    user = models.ForeignKey('authentification.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    video_chapter = models.ForeignKey('Courses.Chapter', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
