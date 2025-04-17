from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    """Get a value from a dictionary using the specified key."""
    return dictionary.get(key, 0)

@register.filter
def div(value, arg):
    """Divide the value by the argument."""
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def mul(value, arg):
    """Multiply the value by the argument."""
    try:
        return float(value) * float(arg)
    except ValueError:
        return 0

@register.filter
def add_class(field, css_class):
    """Add a CSS class to a form field."""
    return field.as_widget(attrs={"class": css_class}) 