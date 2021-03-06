# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-12-31 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_job_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.TextField(blank=True)),
                ('course', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField(blank=True)),
                ('company', models.TextField(blank=True)),
                ('start_date', models.TextField(blank=True)),
                ('end_date', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Education',
            new_name='current_position',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Experience',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Projects',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Profile'),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Profile'),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Profile'),
        ),
    ]
