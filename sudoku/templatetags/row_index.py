from django import template
register = template.Library()

@register.filter
def row_index(List, i):
  return List[int(i)]