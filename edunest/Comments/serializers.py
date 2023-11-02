from rest_framework  import serializers
from .models import *
from authentification.serializers import *

class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class ReplyCreateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class EditDeleteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = '__all__'