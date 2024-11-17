from django.shortcuts import render
import base64
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image

def capture_image(request):
    if request.method == "POST":
        # Get the base64 string from the form data
        image_data = request.POST.get('photo')
        
        # Extract the image data from the base64 string
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        
        # Decode the image data
        image_data = ContentFile(base64.b64decode(imgstr))
        
        # Save the image file
        image = Image.open(image_data)
        file_path = f'captured_image.{ext}'
        image.save(f'media/{file_path}')

        # Return the saved image URL
        return JsonResponse({'message': 'Image captured successfully', 'image_url': f'/media/{file_path}'})

    return render(request, 'mobile/main.html')

