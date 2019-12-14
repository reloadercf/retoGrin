from rest_framework import serializers
from  django.contrib.auth.models import User,  Permission
from .models import Profile, TipoUsuario


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'



class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoUsuario
        fields = '__all__'





class ProfileSerializer(serializers.ModelSerializer):
    tipoUsuario=serializers.PrimaryKeyRelatedField(
	queryset=TipoUsuario.objects.all(),
		required=True,
        many=False)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields =['id', 'tipoUsuario', 'foto', 'slug']

    def update(self, instance, validated_data):
        instance.tipoUsuario = validated_data.get('tipoUsuario', instance.tipoUsuario)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance




class UserSerializer(serializers.ModelSerializer):
    profile_usuario = ProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'user_permissions', 'password', 'is_active','profile_usuario']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_permissions = validated_data.pop('user_permissions')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.user_permissions.set(user_permissions)
        user.save()
        return user 

class UserCortoSerializer(serializers.ModelSerializer):
    profile_usuario=ProfileSerializer(many=False)
    class Meta:
        model=User
        fields=['id','username','first_name', 'last_name', 'profile_usuario']

class SerializerWithoutPasswordField(serializers.ModelSerializer):
    profile_usuario = ProfileSerializer(read_only=True)
    class Meta:
        model=User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'user_permissions', 'is_active','profile_usuario']

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =['id', 'tipoUsuario', 'foto', 'slug']



class UserSerializerComplete(serializers.ModelSerializer):
    profile_usuario = MyProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'user_permissions', 'password', 'is_active','profile_usuario']


class MyUserSerializar(serializers.ModelSerializer):
    profile_usuario = MyProfileSerializer(read_only=True)
    user_permissions=PermissionSerializer(many=True, read_only=True)

    class Meta:
        model=User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'user_permissions', 'profile_usuario']