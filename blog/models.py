from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_NULL
from django.utils import timezone

from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

Usuario = get_user_model()


class Post(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Author',
                              related_name='rn_posts', related_query_name='rqn_posts')
    conteudo = RichTextField()
    likes = models.IntegerField(verbose_name='Likes', default=0)
    publicado_em = models.DateTimeField(
        verbose_name='Publicado em', blank=True, null=True)
    rascunho = models.BooleanField(verbose_name='Rascunho?', default=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.conteudo[:50]

    def publicar(self):
        self.rascunho = False
        self.publicado_em = timezone.now

    def tornar_rascunho(self):
        self.rascunho = True
        self.publicado_em = ''
