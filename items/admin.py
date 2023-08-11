from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ['item_type','is_api_post','api_item_id','item_creator',
	'date_created']
	search_fields = ['item_type',"title",]
	# list_editable = []
	readonly_fields = ['title', 'item_type', 'item_creator',
	 	'date_created', 'is_api_post']

	def has_change_permission(self, request, obj=None):
		if obj and obj.is_api_post:
			return False  # API posts are not editable
		return super().has_change_permission(request, obj)