# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20140710_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddresses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.ForeignKey(to='users.Address')),
                ('user', models.ForeignKey(to='users.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(to=b'users.Address', through='users.UserAddresses'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='primary_address',
            field=models.ForeignKey(default=None, to='users.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=75),
        ),
    ]
