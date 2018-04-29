from django import template
register = template.Library()

@register.filter
def table_array_index(i, j):
  i = int(i)
  j = int(j)
  n = 9
  return i * n + j