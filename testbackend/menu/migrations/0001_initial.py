# Generated by Django 4.2 on 2024-04-14 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название меню.",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=200, verbose_name="слаг"),
                ),
            ],
            options={
                "verbose_name": "меню",
                "verbose_name_plural": "меню",
            },
        ),
        migrations.CreateModel(
            name="MenuSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("left", models.PositiveIntegerField(default=1)),
                ("right", models.PositiveIntegerField(default=2)),
                ("level", models.PositiveIntegerField(default=0)),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название меню.",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                ("url", models.SlugField(max_length=200, verbose_name="слаг")),
                (
                    "is_named_url",
                    models.BooleanField(
                        default=False,
                        help_text="Если это обычная ссылка, то нет, иначе да.",
                        verbose_name="is_named_url",
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        help_text="...",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="menu.menu",
                        verbose_name="меню секции",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="...",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="down_sections",
                        to="menu.menusection",
                        verbose_name="верхняя секция",
                    ),
                ),
            ],
            options={
                "verbose_name": "секция меню",
                "verbose_name_plural": "секции меню",
                "abstract": False,
            },
        ),
    ]


__all__ = ()
