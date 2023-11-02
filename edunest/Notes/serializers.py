from rest_framework import serializers
from  .models import *
from Courses.serializers import ChapterSerializer

class NoteSerializerAdd(serializers.ModelSerializer):
    print('raeched serializers==================================================================')
    class Meta:
        model = Note
        fields = ['id', 'chapter', 'timestamp', 'content', 'created_at']

class NoteSerializer(serializers.ModelSerializer):
    chapter_details = ChapterSerializer(source='chapter', read_only=True)

    class Meta:
        model = Note
        fields = '__all__' 