from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    """Adiciona a classe CSS ao campo de formulário"""
    return value.as_widget(attrs={'class': class_name})