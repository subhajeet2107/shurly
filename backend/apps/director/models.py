from django.db import models

from apps.users.models import User


class Director(models.Model):
    original_url = models.URLField(verbose_name='Original Url', unique=True, max_length=255, db_index=True)
    short_url = models.URLField(verbose_name='Shortened Url', unique=True, max_length=255, db_index=True)

    added_by = models.ForeignKey(User, verbose_name='Added By', null=True, blank=True, on_delete=models.SET_NULL)
    added_on = models.DateTimeField(verbose_name='Added at', auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

    def __str__(self):
        return f'self.original_url -> self.short_url'
