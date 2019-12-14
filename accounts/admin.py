
from .models import Profile
from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import TipoUsuario



admin.site.register(Profile)
admin.site.register(TipoUsuario)
admin.site.register(Permission)