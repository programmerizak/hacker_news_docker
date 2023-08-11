from django import template
from items.forms import ItemSearchForm

register = template.Library()

@register.inclusion_tag('search_form.html')
def search_form():
	form = ItemSearchForm()
	return {'form': form}
