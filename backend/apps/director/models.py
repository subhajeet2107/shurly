from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from apps.director.helper import CustomHasher


class Director(models.Model):
    original_url = models.URLField(verbose_name='Original Url', unique=True, max_length=255, db_index=True)
    short_url = models.URLField(verbose_name='Short Url', unique=True, max_length=255, db_index=True)
    short_url_hash = models.CharField(verbose_name='Short Url Hash', unique=True, max_length=10, db_index=True)
    hits = models.PositiveIntegerField(verbose_name='Url hits counter', default=0)

    added_by = models.ForeignKey(User, verbose_name='Added By', null=True, blank=True, on_delete=models.SET_NULL)
    added_on = models.DateTimeField(verbose_name='Added at', auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

    def __str__(self):
        return '{0} -> {1}'.format(self.original_url, self.short_url)


@receiver(post_save, sender=Director)
def generate_shortened_url(sender, instance=None, created=False, **kwargs):

    if created:
        custom_hasher = CustomHasher(instance.id)
        short_url_hash = custom_hasher.encode()
        short_url = settings.BASE_URL + short_url_hash
        Director.objects.filter(id=instance.id).update(short_url_hash = short_url_hash, short_url=short_url)
