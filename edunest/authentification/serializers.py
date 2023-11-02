from rest_framework  import serializers
from .models import *
 
class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'profile_image', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','role','id','profile_image' )



# class UserRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
        
#         fields = ('temp_role','role')

