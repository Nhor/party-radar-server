# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import api.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=api.models.get_post_image_upload_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
