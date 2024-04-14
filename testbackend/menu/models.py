from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.expressions import Case, F, When
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from core.models import NodeAbstract
from menu.manager import MenuSectionsManager


class Menu(models.Model):
    name = models.CharField(
        verbose_name="название",
        max_length=150,
        help_text="Укажите название меню.",
        unique=True,
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name="слаг",
    )

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню"


class MenuSection(NodeAbstract):
    objects = MenuSectionsManager()

    name = models.CharField(
        "название",
        max_length=150,
        help_text="Укажите название меню.",
        unique=True,
    )
    url = models.SlugField(
        max_length=200,
        verbose_name="слаг",
    )
    is_named_url = models.BooleanField(
        default=False,
        verbose_name="is_named_url",
        help_text="Если это обычная ссылка, то нет, иначе да.",
    )
    parent = models.ForeignKey(
        "self",
        related_name="down_sections",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
        verbose_name="верхняя секция",
        help_text="...",
    )
    menu = models.ForeignKey(
        Menu,
        related_name="sections",
        on_delete=models.CASCADE,
        verbose_name="меню секции",
        help_text="...",
    )

    def clean(self):
        super().clean()
        if self.is_named_url:
            try:
                reverse(self.url)
            except NoReverseMatch:
                raise ValidationError(
                    "Вы указали не правильный слаг!",
                )
        if self.parent and self.parent not in self.menu.sections.all():
            raise ValidationError("Секция должна быть из укзанного меню!")
        if self == self.parent:
            raise ValidationError("Секция не может выходить из самой себя!")

    def save(self, *args, **kwargs):
        if self.parent:
            add_child(self.parent, self)
        super().save(*args, **kwargs)

    class Meta(NodeAbstract.Meta):
        verbose_name = "секция меню"
        verbose_name_plural = "секции меню"


def add_child(parent: MenuSection, child: MenuSection):
    MenuSection.objects.filter(
        right__gte=parent.right,
        menu=parent.menu,
    ).update(
        left=Case(
            When(
                left__gt=parent.right,
                then=F("left") + 2,
            ),
            default=F("left"),
            output_field=models.PositiveIntegerField(),
        ),
        right=F("right") + 2,
    )
    child.left = parent.right
    child.right = parent.right + 1
    child.level = parent.level + 1


__all__ = ()
