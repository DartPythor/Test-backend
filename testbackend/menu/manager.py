from django.db.models import Manager


class MenuSectionsManager(Manager):
    def get_all_tree(self, node):
        return (
            super()
            .get_queryset()
            .filter(
                left__gte=node.left,
                right__lte=node.right,
            )
        )


__all__ = ()
