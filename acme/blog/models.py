from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

class TimespantedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Post(TimespantedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.CharField(max_length=255, default='http://www.generation-voyageurs.com/wp-content/uploads/2017/08/2-plage-600x400.jpg')

    def __str__(this):
        return this.title

class Comment(TimespantedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __unicode__(this):
        return str(this.user.username)
    def __str__(this):
        return str(this.user.username)
