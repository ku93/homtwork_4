from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def time_since(value):
    if value:
        delta = timezone.now() - value
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        if days > 0:
            return f"{days} день(дня)" if days == 1 else f"{days} дней"
        elif hours > 0:
            return f"{hours} час(а)" if hours == 1 else f"{hours} часов"
        elif minutes > 0:
            return f"{minutes} минут(ы)" if minutes == 1 else f"{minutes} минут"
        else:
            return "только что"
    return "недавно"