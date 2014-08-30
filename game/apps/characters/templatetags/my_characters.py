from game.apps.characters.models import Character
from django import template

register = template.Library()

@register.inclusion_tag("site/my_characters.html", takes_context=True)
def my_characters(context):
    request = context['request']
    my_characters = Character.objects.filter(user=request.user).order_by('-name')
    return {
        "my_characters": my_characters,
        "request": request
    }
