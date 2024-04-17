from django import template


from menu.models import MenuSection

register = template.Library()


@register.inclusion_tag("menu/tree.html", takes_context=True)
def draw_menu(context, menu):
    sections = MenuSection.objects.get_all_tree(menu)

    current_section = sections.filter(
        url=context["request"].resolver_match.view_name,
    )

    if current_section.count() == 0:
        current_section = sections.filter(
            url=context["request"].path,
        )
    if current_section.count() == 0:
        return {"tree": sections.filter(parent=None), "name_menu": menu}
    current_section = current_section[0]
    open_sections = get_open_sections(current_section)
    main_parent = sections.filter(parent=None)

    for parent in main_parent:
        if parent.id in open_sections:
            parent.child = get_child(sections, parent.id, open_sections)

    return {"tree": main_parent, "name_menu": menu}


def get_open_sections(parent):
    open_sections = []
    while parent.parent:
        open_sections.append(parent.id)
        parent = parent.parent
    open_sections.append(parent.id)
    return open_sections


def get_child(section, current_parent_id, open_section):
    current_parent_child = section.filter(parent_id=current_parent_id)
    for child in current_parent_child:
        if child.id in open_section:
            child.child = get_child(section, child.id, open_section)
    return current_parent_child


__all__ = ()
