from django.core.mail import send_mail
from django.utils import timezone
import datetime
import random
from rest_framework.decorators import APIView
from rest_framework.response import Response
from authentification.serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied



class UserRegistrationView(APIView):

    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            otp = ''.join(random.choices('0123456789', k=6))
            user.otp = otp
            user.otp_created_at = timezone.now()
            user.save()
            print(user.username)
            print(user.email)

            send_mail(
                'Your OTP Code',
                f'Your OTP code is: {otp}',
                'from_email@example.com',  
                [user.email],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckUsernameView(APIView):

    def get(self, request):
        username = request.query_params.get('username')
        if not username:
            return Response({"error": "Missing username parameter"}, status=status.HTTP_400_BAD_REQUEST)

        isAvailable = not CustomUser.objects.filter(username=username).exists()
        return Response({"isAvailable": isAvailable}, status=status.HTTP_200_OK)
    

class VerifyOTPView(APIView):

    def post(self, request):
        username = request.data.get('username')
        otp = request.data.get('otp')
        
        user = CustomUser.objects.filter(username=username).first()

        if not user:
            return Response({"detail": "User not found."}, status=status.HTTP_400_BAD_REQUEST)

        otp_validity = datetime.timedelta(minutes=5)
        if user.otp == otp and timezone.now() - user.otp_created_at <= otp_validity:
            user.otp = None
            user.is_verified = True
            user.save()
            return Response({"detail": "OTP verified successfully!"})
        else:
            return Response({"detail": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

class CustomUserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.exclude(role='TEACHER')
    serializer_class = CustomUserSerializer
 

# class GetUserRoleView(generics.RetrieveAPIView):
#     serializer_class = UserRoleSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user

class GetUserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user.role,'============================================')
        if user.role == 'BAN':
            raise PermissionDenied("Admin has blocked you")
        return Response({'role': user.role, 'temp_role': user.temp_role,'user_id': user.id})
    
class SwitchRoleView(APIView):
        permission_classes = [IsAuthenticated] 
        def post(self, request):
                user = request.user

                if user.role == CustomUser.TEACHER:
                    if user.temp_role == CustomUser.USER:
                        user.temp_role = CustomUser.TEACHER
                    else:
                        user.temp_role = CustomUser.USER
                elif user.role == CustomUser.ADMIN:
                    if user.temp_role == CustomUser.USER:
                        user.temp_role = CustomUser.ADMIN
                    else:
                        user.temp_role = CustomUser.USER
                user.save()
                return Response({"status": "Role switched successfully", "new_role": user.temp_role})

class UpdateFacultyRoleView(APIView):
    
    def patch(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        role = request.data.get('role', None)

        if role in ['BAN', 'TEACHER']:
            user.role = role
            user.save()
            action = "banned" if role == "BAN" else "unblocked"
            return Response({"message": f"User {action} successfully!"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid role provided."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        
        print('reached ')
        try:
            refresh_token = request.data["refresh_token"]
            print(refresh_token,'reached ')
        #     token = RefreshToken(refresh_token)
        #     print(token,'reached ')
        #     token.blacklist()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)            
          

            