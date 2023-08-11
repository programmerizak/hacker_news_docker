from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .serializers import ItemSerializer, ItemFilterSerializer
from items.models import Item


class ItemCRUD(APIView):

	########## RETRIEVE ALL ITEMS ############################
	def get(self, request, pk=None):
		if pk is None:
			filter_serializer = ItemFilterSerializer(data=request.query_params)
			filter_serializer.is_valid(raise_exception=True)
			filters = filter_serializer.validated_data

			query = Q()

			if 'category' in filters:
				if filters['category']:
					query &= Q(item_type=filters['category'])

			if filters.get('search_in_creator', False):
				query |= Q(item_creator__icontains=filters.get('query', ''))

			if filters.get('search_in_score', False):
				query |= Q(score__icontains=filters.get('query', ''))

			items = Item.objects.filter(query)
			serializer = ItemSerializer(items, many=True)
			return Response(serializer.data)
		else:
			try:
				item = Item.objects.get(pk=pk)
				serializer = ItemSerializer(item)
				return Response(serializer.data)
			except Item.DoesNotExist:
				return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

	########## CREATING NEW ITEM ############################
	def post(self, request):
		serializer = ItemSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	####### COMPLETE UPDATING ITEM(item_type compulsory) #########
	def put(self, request, pk):
		try:
			item = Item.objects.get(pk=pk, is_api_post=False)
		except Item.DoesNotExist:
			return Response({'detail': 'Item not found or not editable.'}, status=status.HTTP_404_NOT_FOUND)

		serializer = ItemSerializer(item, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	####### PARTIAL UPDATING OF ITEM(item_type not compulsory) ###########
	def patch(self, request, pk):
		try:
			item = Item.objects.get(pk=pk, is_api_post=False)
		except Item.DoesNotExist:
			return Response({'detail': 'Item not found or not editable.'}, status=status.HTTP_404_NOT_FOUND)

		serializer = ItemSerializer(item, data=request.data, partial=True)  # Use partial=True for partial updates
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	########## DELETING ITEM ############################
	def delete(self, request, pk):
		try:
			item = Item.objects.get(pk=pk, is_api_post=False)
		except Item.DoesNotExist:
			return Response({'detail': 'Item not found or not editable.'}, status=status.HTTP_404_NOT_FOUND)

		item.delete()
		return Response({'detail': 'Item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)