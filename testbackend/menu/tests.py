from django.test import TestCase

from menu.models import Menu, MenuSection


class TestCreation(TestCase):
    def test_creation_menu(self):
        count_obj = Menu.objects.count()
        menu = Menu(
            name="TestMenu",
        )
        menu.save()
        self.assertEqual(count_obj + 1, Menu.objects.count())

    def test_creation_section(self):
        menu = Menu(
        )
        menu.save()

        count_obj = MenuSection.objects.count()
        section = MenuSection(
            name="TestSectionParent",
            url="https://test",
            menu=menu,
        )
        section.save()
        self.assertEqual(count_obj + 1, MenuSection.objects.count())


__all__ = ()
