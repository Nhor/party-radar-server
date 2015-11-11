from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


def get_post_image_upload_path(instance, filename):
    user = instance.user.username
    uuid = uuid4().replace('-', '')
    ext = filename.split('.')[1]
    return '{0}/images/{1}.{2}'.format(user, uuid, ext)


class Post(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to=get_post_image_upload_path)
    description = models.TextField(blank=True, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
