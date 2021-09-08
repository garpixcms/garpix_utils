from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """
    Подмена одного значения в dict на другое в Django-шаблонах.
    Применять можно так:
        {% url_replace request 'page' page_num %}
    """
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
