from django import template
register = template.Library()

@register.filter
def table_row(List, i):
  n = 9
  i = int(i)
  return List[i*n:i*n+n]