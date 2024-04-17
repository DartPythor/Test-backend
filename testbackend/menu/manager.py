from django.db.models import Manager


class MenuSectionsManager(Manager):
    def get_all_tree(self, menu_name):
        return (
            super()
            .get_queryset()
            .select_related("parent")
            .filter(
                menu__name=menu_name,
            )
        )


__all__ = ()
