from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, FileResponse
from django.urls import reverse
from .models import Image, Producto
import json
import mimetypes

def index(request):
    pics = Image.objects.all()
    return render(request,'index.html',{'pics': pics})

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
        'carbs': str(producto.carbs) if producto.carbs is not None else None,
        'fat': str(producto.fat) if producto.fat is not None else None,
        'protein': str(producto.protein) if producto.protein is not None else None,
        'salt': str(producto.salt) if producto.salt is not None else None,
        'price': str(producto.price) if producto.price is not None else None,
        'stock': producto.stock,
        'image_url': request.build_absolute_uri(reverse('get_product_image', args=[producto.image.id])) if producto.image else None,
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