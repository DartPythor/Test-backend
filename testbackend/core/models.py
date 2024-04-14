from django.db import models


class NodeAbstract(models.Model):
    left = models.PositiveIntegerField(default=1)
    right = models.PositiveIntegerField(default=2)
    level = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        abstract = True


__all__ = ()
