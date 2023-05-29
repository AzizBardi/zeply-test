from django.urls import path
from rest_framework import permissions
from crypto_address_generator.views import GenerateAddressView, ListAddressView, RetrieveAddressView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Cryptocurrency Address API",
        default_version='v1',
        description="API for generating and retrieving cryptocurrency addresses",
        contact=openapi.Contact(email="bardiaziz@yahoo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('address/generate/', GenerateAddressView.as_view(), name='generate-address'),
    path('address/list/', ListAddressView.as_view(), name='list-addresses'),
    path('address/<int:id>/', RetrieveAddressView.as_view(), name='retrieve-address'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
