from django import template

register = template.Library()

@register.filter
def get_attribute_by_name(obj, name):
    return obj.get_attribute_by_name(name)
