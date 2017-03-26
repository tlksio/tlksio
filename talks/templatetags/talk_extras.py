from django import template
register = template.Library()

@register.filter(name='has_favorited')
def has_favorited(talk,user_id):
    return talk.favorites.filter(id=user_id).count() > 0

@register.filter(name='has_voted')
def has_voted(talk,user_id):
    return talk.votes.filter(id=user_id).count() > 0


