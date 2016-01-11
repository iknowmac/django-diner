# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe', verbose_name='recipe'),
            preserve_default=False,
        ),
    ]
