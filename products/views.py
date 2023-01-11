from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import productsSerializer


@api_view(["GET"])
def Produc_list(request):

    products = Products.objects.all()
    
    serializer = productsSerializer(products, many = True)


    return Response (serializer.data)
