from django.http import JsonResponse
from rest_framework import generics

from .currency.manager import CoinManager
from .models import Address
from .serializers import AddressSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


class GenerateAddressView(generics.CreateAPIView):
    serializer_class = AddressSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('multiple', openapi.IN_QUERY, description='Number of addresses to generate',
                          type=openapi.TYPE_INTEGER, multiple=True)])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        currency = serializer.validated_data['currency']
        manager = CoinManager()
        multiple = request.query_params.get('multiple', False)
        if multiple:
            try:
                addresses = manager.generate_multi_addresses(currency, int(multiple))
                for address in addresses:
                    serializer = self.serializer_class(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.validated_data["address"] = address
                    serializer.save()
            except ValueError:
                return JsonResponse({'success': False, 'error': 'Invalid multiple value'}, status=400)
        else:
            address = manager.generate_address(currency)
            serializer.validated_data["address"] = address
            serializer.save()
        return JsonResponse({"success": True})


class ListAddressView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RetrieveAddressView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'
