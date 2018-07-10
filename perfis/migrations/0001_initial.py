# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=b'255')),
                ('email', models.CharField(max_length=b'255')),
                ('telefone', models.CharField(max_length=b'15')),
                ('nome_empresa', models.CharField(max_length=b'255')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
