from rest_framework import viewsets, generics
from rest_framework.views import APIView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User, Permission
from rest_framework.response import Response
from rest_framework.mixins import(
    DestroyModelMixin,
    UpdateModelMixin
)

from .serializer import (
ProfileSerializer,
UserSerializer,
MyUserSerializar,
PermissionSerializer,
SerializerWithoutPasswordField,
UserSerializerComplete,
TipoUsuarioSerializer

)

from django.db.models import Q
from .models import (
    Profile,
    TipoUsuario
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

from rest_framework.filters import (
  SearchFilter,
  OrderingFilter
)



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        uid= token.key
        custom_token=auth.create_custom_token(uid)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == ['PUT', 'PATCH']:
            serializer_class = SerializerWithoutPasswordField
        return serializer_class
    
    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        nombre = self.request.GET.get("nombre")
        if nombre:
            queryset_list = queryset_list.filter(
                Q(first_name__contains=nombre)|
                Q(last_name__contains=nombre)|
                Q(username__contains=nombre)
            )
        return  queryset_list


    

    
class PermisosViewSet(viewsets.ModelViewSet):
  queryset = Permission.objects.all().filter(content_type=10)
  serializer_class = PermissionSerializer


class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'

def get_queryset(self, *args, **kwargs):
		slug = self.request.GET.get('slug')
		queryset_list = super(ProfileViewSet,self).get_queryset()
		if slug:
			queryset_list = queryset_list.filter(slug=slug)
		return queryset_list

class PerfilViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
       

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class MyUser(APIView):
    def get(self, request, format=None):
        my_user = User.objects.all().get(id=request.user.id)
        serializer = MyUserSerializar(my_user)
        return Response(serializer.data)


class UserCompleteView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerComplete
