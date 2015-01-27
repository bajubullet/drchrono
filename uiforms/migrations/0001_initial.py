# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_type', models.CharField(max_length=5, verbose_name='field type', choices=[(b'bool', b'Boolean Field'), (b'int', b'Integer Field')])),
                ('field_name', models.CharField(max_length=50, verbose_name='field name')),
                ('field_label', models.CharField(max_length=255, null=True, verbose_name='field label', blank=True)),
                ('field_desc', models.TextField(null=True, verbose_name='field description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UiForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='formfields',
            name='form',
            field=models.ForeignKey(verbose_name='form', to='uiforms.UiForm'),
            preserve_default=True,
        ),
    ]
