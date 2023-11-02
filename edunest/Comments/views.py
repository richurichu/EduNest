from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class CommentViewSet(viewsets.ModelViewSet):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        if chapter_id:
            return Comment.objects.filter(video_chapter=chapter_id)
        else:
           
            return Comment.objects.none()
    
    # def post(self, request, chapter_id,user):
      
    #     data = request.data
        
    #     data['user'] = user  
    #     data['video_chapter'] = chapter_id

    #     serializer = CommentSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, chapter_id):
        text = request.data.get('text')
        chapter = Chapter.objects.get(pk=chapter_id)
        user = request.user  # This is the authenticated user
        if request.data.get('parentid'):
             
             id = request.data.get('parentid')
             print(id,'===================================================')
             parent = Comment.objects.get(pk=id)

             comment = Comment.objects.create(
             user=user,
             video_chapter=chapter,
             text=text,
             parent_comment = parent
        )

             serializer = CommentCreateSerializer(comment)

             return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Create a new comment with the provided data
        comment = Comment.objects.create(
            user=user,
            video_chapter=chapter,
            text=text
        )

        serializer = CommentCreateSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ReplyCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, chapter_id):
        text = request.data.get('text')
        id = request.data.get('parentid')
        chapter = Chapter.objects.get(pk=chapter_id)
        user = request.user  # This is the authenticated user
        
        print(id,'===================================================')
        parent = Comment.objects.get(pk=id)

        comment = Comment.objects.create(
        user=user,
        video_chapter=chapter,
        text=text,
        parent_comment = parent)
        

        serializer = ReplyCreateSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CommentEditDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = EditDeleteSerializer
    lookup_field = 'id'
  