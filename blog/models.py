from django.conf import settings
from django.db import models
from django.utils import timezone
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


def replace_space(title):
    return title.replace(" ", "-").lower()


@receiver(pre_save, sender=Post)
def generation_slug(sender, instance, **kwargs):
    if (instance.id is None) or (instance.slug != replace_space(instance.title)):
        instance.slug = replace_space(instance.title)
