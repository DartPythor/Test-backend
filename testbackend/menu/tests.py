from django.test import TestCase

from menu.models import Menu, MenuSection


class TestCreation(TestCase):
    def test_creation_menu(self):
        count_obj = Menu.objects.count()
        menu = Menu(
            name="TestMenu",
            slug="https://test",
        )
        menu.save()
        self.assertEqual(count_obj + 1, Menu.objects.count())

    def test_creation_section(self):
        menu = Menu(
            name="TestMenu",
            slug="https://test",
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


class TestSectionInsert(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.menu1 = Menu(
            name="TestMenu1",
            slug="https://test",
        )
        cls.menu1.save()

        cls.section_parent = MenuSection(
            name="TestSectionParent",
            url="https://test",
            menu=cls.menu1,
        )
        cls.section_parent.save()

    def test_insertion(self):
        new_section = MenuSection(
            name="TestSection",
            url="url",
            menu=self.menu1,
            parent=self.section_parent,
            left=1,
            right=2,
        )
        new_section.save()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 4)

        self.assertEqual(new_section.level, 1)
        self.assertEqual(new_section.left, 2)
        self.assertEqual(new_section.right, 3)

    def test_insertion_tree(self):
        section1 = MenuSection(
            name="TestSection1",
            url="url",
            menu=self.menu1,
            parent=self.section_parent,
        )
        section1.save()

        section1.refresh_from_db()
        self.section_parent.refresh_from_db()
        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 4)
        self.assertEqual(section1.left, 2)
        self.assertEqual(section1.right, 3)

        section2 = MenuSection(
            name="TestSection2",
            url="url",
            menu=self.menu1,
            parent=section1,
        )
        section2.save()
        section1.refresh_from_db()
        section2.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 6)
        self.assertEqual(section1.left, 2)
        self.assertEqual(section1.right, 5)
        self.assertEqual(section2.left, 3)
        self.assertEqual(section2.right, 4)

        section3 = MenuSection(
            name="TestSection3",
            url="url",
            menu=self.menu1,
            parent=section1,
        )
        section3.save()
        section1.refresh_from_db()
        section2.refresh_from_db()
        section3.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 8)
        self.assertEqual(self.section_parent.level, 0)
        self.assertEqual(section1.left, 2)
        self.assertEqual(section1.right, 7)
        self.assertEqual(section1.level, 1)
        self.assertEqual(section2.left, 3)
        self.assertEqual(section2.right, 4)
        self.assertEqual(section2.level, 2)
        self.assertEqual(section3.left, 5)
        self.assertEqual(section3.right, 6)
        self.assertEqual(section3.level, 2)

    def test_insertion_2tree(self):
        section_parent_1 = MenuSection(
            name="TestSection1Parent",
            url="url",
            menu=self.menu1,
            parent=self.section_parent,
        )
        section_parent_1.save()
        section_parent_1.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 4)
        self.assertEqual(section_parent_1.left, 2)
        self.assertEqual(section_parent_1.right, 3)

        section_parent_2 = MenuSection(
            name="TestSection2Parent",
            url="url",
            menu=self.menu1,
            parent=self.section_parent,
        )
        section_parent_2.save()
        section_parent_2.refresh_from_db()
        section_parent_1.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 6)
        self.assertEqual(section_parent_1.left, 2)
        self.assertEqual(section_parent_1.right, 3)
        self.assertEqual(section_parent_2.left, 4)
        self.assertEqual(section_parent_2.right, 5)

        section1 = MenuSection(
            name="TestSection1",
            url="url",
            menu=self.menu1,
            parent=section_parent_1,
        )
        section1.save()
        section1.refresh_from_db()
        section_parent_1.refresh_from_db()
        section_parent_2.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 8)
        self.assertEqual(section_parent_1.left, 2)
        self.assertEqual(section_parent_1.right, 5)
        self.assertEqual(section_parent_2.left, 6)
        self.assertEqual(section_parent_2.right, 7)

        section2 = MenuSection(
            name="TestSection12",
            url="url",
            menu=self.menu1,
            parent=section_parent_1,
        )
        section2.save()
        section2.refresh_from_db()
        section1.refresh_from_db()
        section_parent_1.refresh_from_db()
        section_parent_2.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 10)
        self.assertEqual(section_parent_1.left, 2)
        self.assertEqual(section_parent_1.right, 7)
        self.assertEqual(section_parent_2.left, 8)
        self.assertEqual(section_parent_2.right, 9)

        section3 = MenuSection(
            name="TestSection2",
            url="url",
            menu=self.menu1,
            parent=section_parent_2,
        )
        section3.save()
        section3.refresh_from_db()
        section2.refresh_from_db()
        section1.refresh_from_db()
        section_parent_1.refresh_from_db()
        section_parent_2.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(self.section_parent.left, 1)
        self.assertEqual(self.section_parent.right, 12)
        self.assertEqual(section_parent_1.left, 2)
        self.assertEqual(section_parent_1.right, 7)
        self.assertEqual(section1.left, 3)
        self.assertEqual(section1.right, 4)
        self.assertEqual(section2.left, 5)
        self.assertEqual(section2.right, 6)
        self.assertEqual(section_parent_2.left, 8)
        self.assertEqual(section_parent_2.right, 11)
        self.assertEqual(section3.left, 9)
        self.assertEqual(section3.right, 10)

        section4 = MenuSection(
            name="TestSection3",
            url="url",
            menu=self.menu1,
            parent=section_parent_2,
        )
        section4.save()
        section4.refresh_from_db()
        section3.refresh_from_db()
        section2.refresh_from_db()
        section1.refresh_from_db()
        section_parent_2.refresh_from_db()
        section_parent_1.refresh_from_db()
        self.section_parent.refresh_from_db()
        self.assertEqual(section4.left, 11)
        self.assertEqual(section4.right, 12)

        section5 = MenuSection(
            name="TestSection4",
            url="url",
            menu=self.menu1,
            parent=section_parent_2,
        )
        section5.save()

        section5.refresh_from_db()
        section4.refresh_from_db()
        section3.refresh_from_db()
        section2.refresh_from_db()
        section1.refresh_from_db()
        section_parent_2.refresh_from_db()
        section_parent_1.refresh_from_db()
        self.section_parent.refresh_from_db()

        self.assertEqual(section5.left, 13)
        self.assertEqual(section5.right, 14)

        qs = MenuSection.objects.get_all_tree(self.section_parent)
        self.assertEqual(qs.count(), 8)


__all__ = ()
