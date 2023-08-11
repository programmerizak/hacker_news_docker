from rest_framework import serializers
from items.models import Item



# class UpdateItemSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Item
# 		fields = ['title', 'text', 'item_type', 'item_creator', 'date_created']


# class DeleteItemSerializer(serializers.Serializer):
# 	item_id = serializers.IntegerField()



class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'



class ItemFilterSerializer(serializers.Serializer):
	category = serializers.ChoiceField(
		choices=[
			('', 'All'),
			('jobs', 'Jobs'),
			('story', 'Story'),
			('comment', 'Comment'),
			('poll', 'Poll'),
		],
		required=False,  # Make the category field optional
	)
	search_in_creator = serializers.BooleanField(required=False)
	search_in_score = serializers.BooleanField(required=False)
	query = serializers.CharField(required=False)  # Add query field for searching

