from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
	openapi.Info(
		title="My Project API",
		default_version='v1',
		description="API documentation for Hacker News V2.0",
		terms_of_service="https://www.isaac.com/terms/",
		contact=openapi.Contact(email="isaac@isaac.com"),
		license=openapi.License(name="Imafidon Isaac"),
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
