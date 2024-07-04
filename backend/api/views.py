from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, FileResponse
from django.urls import reverse
from django.conf import settings
from .models import Image, Producto
from .serializers import UserSerializer, ProductSerializer
import json
import mimetypes

# Admin views
def index(request):
    pics = Image.objects.all()
    return render(request,'index.html',{'pics': pics})

class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    queryset = Producto.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid:
            serializer.save()
        else:
            print(f"[ERROR] - {serializer.errors}")

class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    queryset = Producto.objects.all()



# User views 
def products(response):
    products = Producto.objects.all().values()
    return JsonResponse(list(products), safe=False)

def product_details(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto_dict = {
        'id': producto.id,
        'name': producto.name,
        'description': producto.description,
        'storage': producto.storage,
        'carbs': str(producto.carbs) if producto.carbs else None,
        'fat': str(producto.fat) if producto.fat else None,
        'protein': str(producto.protein) if producto.protein else None,
        'salt': str(producto.salt) if producto.salt else None,
        'price': str(producto.price) if producto.price else None,
        'stock': producto.stock,
        'image_id': producto.image_id if producto.image_id else None,
        'image_url': request.build_absolute_uri(
            reverse('get_product_image', args=[producto.image.id])
            ) if producto.image else 
            request.build_absolute_uri(settings.MEDIA_URL + 'img/24/not-found.jpg')
    }
    return JsonResponse(producto_dict)
    
def get_product_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image_path = image.image.path
    with open(image_path, 'rb') as f:
        image_data = f.read()
    content_type, _ = mimetypes.guess_type(image_path)
    return FileResponse(open(image_path, 'rb'), content_type=content_type)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def update_stock(request):
    if request.method.upper() == 'POST':
        try:
            data = json.loads(request.body)
            for item in data['cart']:
                product = Producto.objects.get(id=item['id'])
                product.stock -= item['quantity']
                product.save()
            return JsonResponse({'message': 'Stock updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'Error updating stock: {str(e)}'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]