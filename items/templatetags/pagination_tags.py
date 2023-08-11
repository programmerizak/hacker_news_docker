from django import template

'''
NOTE: That since am using one pagination alround, the values return by the 
functions must be called items for the pagination to work
'''

register = template.Library()

@register.inclusion_tag('pagination.html')
def render_pagination(items):
	return {'items': items}
