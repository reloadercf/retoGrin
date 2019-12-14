from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
  



class TipoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=100)

    def __str__(self):
       return self.tipo_usuario


class Profile(models.Model):
    usuario         = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_usuario')
    tipoUsuario     = models.ForeignKey(TipoUsuario, related_name='usuario_tipo', on_delete=models.CASCADE, blank=True, null=True)
    foto            = models.TextField(null=True, blank=True, max_length=500)
    slug            = models.SlugField(unique=True, blank=True)

    class Meta:
        permissions = (
            ("gerente",   "gerente"),
            ("administrativo",    "administrativo"),
            ("usuario",      "usuario"),
        )


    def __str__(self):
        return self.usuario.username
    @property
    def username(self):
        return self.usuario.username
    @property
    def nombre_completo(self):
        return '%s %s' % (self.usuario.first_name, self.usuario.last_name)


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Profile)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(usuario=kwargs.get('instance'))

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

