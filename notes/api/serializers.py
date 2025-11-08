from rest_framework import serializers
from .models import Note, User

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    email=serializers.EmailField(required=True)
    class Meta:
        model=User
        fields=('id','username','email','password')
        
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')
        
class NoteSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Note
        fields=('user','name','subtask','created_at','updated_at','id',)
        read_only_fields=('created_at','updated_at','id','user')