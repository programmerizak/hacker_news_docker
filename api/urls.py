from django.urls import path, include
from .views import ItemCRUD

app_name = "api"

urlpatterns = [
	path('items/', ItemCRUD.as_view(), name='api_crud'),
	path('items/<uuid:pk>/', ItemCRUD.as_view(), name='api_crud_single'),
	path('docs/', include('api.docs')),  # API documentation URLs
]