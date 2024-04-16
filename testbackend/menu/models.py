from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from menu.manager import MenuSectionsManager


class Menu(models.Model):
    name = models.CharField(
        verbose_name="название",
        max_length=150,
        help_text="Укажите название меню.",
        unique=True,
    )

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню"


class MenuSection(models.Model):
    objects = MenuSectionsManager()

    name = models.CharField(
        "название",
        max_length=150,
        help_text="Укажите название меню.",
        unique=True,
    )
    url = models.SlugField(
        max_length=200,
        verbose_name="ссылка",
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
        help_text="Выберите из какой секции будет выходить секция.",
    )
    menu = models.ForeignKey(
        Menu,
        related_name="sections",
        on_delete=models.CASCADE,
        verbose_name="меню секции",
        help_text="Выберите из какого меню будет выходить секция.",
    )

    def __str__(self):
        return self.name

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
            raise ValidationError("Секция должна быть из указанного меню!")
        if self == self.parent:
            raise ValidationError("Секция не может выходить из самой себя!")

    class Meta:
        verbose_name = "секция меню"
        verbose_name_plural = "секции меню"


__all__ = ()
