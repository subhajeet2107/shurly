# Generated by Django 2.1.7 on 2019-06-15 16:39

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
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(db_index=True, max_length=255, unique=True, verbose_name='Original Url')),
                ('short_url', models.URLField(db_index=True, max_length=255, unique=True, verbose_name='Short Url')),
                ('short_url_hash', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='Short Url Hash')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Url hits counter')),
                ('added_on', models.DateTimeField(auto_now_add=True, verbose_name='Added at')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
    ]
