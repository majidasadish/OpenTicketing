# Generated by Django 2.2.5 on 2020-01-31 16:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('write_date', models.DateTimeField(blank=True, null=True, verbose_name='Last modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('active', models.BooleanField(verbose_name='Is Active')),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_create_uid', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_write_uid', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'db_table': 'ot_organization',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('write_date', models.DateTimeField(blank=True, null=True, verbose_name='Last modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('active', models.BooleanField(verbose_name='Is Active')),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_create_uid', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_write_uid', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'db_table': 'ot_department',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('write_date', models.DateTimeField(blank=True, null=True, verbose_name='Last modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_create_uid', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_write_uid', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'ot_category',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('write_date', models.DateTimeField(blank=True, null=True, verbose_name='Last modified')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('body', models.TextField(verbose_name='Body')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_app.Department', verbose_name='Category')),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogpost_create_uid', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogpost_write_uid', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'db_table': 'op_blogpost',
            },
        ),
    ]
