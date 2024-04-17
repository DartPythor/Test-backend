from django.contrib import admin

from menu.models import Menu, MenuSection


class MenuSectionInline(admin.TabularInline):
    model = MenuSection


@admin.register(Menu)
class MenuModel(admin.ModelAdmin):
    inlines = (MenuSectionInline,)


admin.site.register(MenuSection)

__all__ = ()
