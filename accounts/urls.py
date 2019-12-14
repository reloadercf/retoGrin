from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from .views import *
from django.conf import settings

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)
router.register('permisos', PermisosViewSet)
router.register('tipoUsuario', TipoUsuarioViewSet)
router.register('perfil-sucursal', PerfilViewSet)



accounts = [
    path('apis/', include(router.urls)),
    path('my_user/', MyUser.as_view()),
    path('usercomplete/', UserCompleteView.as_view()),
 

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
]