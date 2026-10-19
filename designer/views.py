import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RoomLayout

def canvas_view(request):
    return render(request, 'designer/canvas.html')

@csrf_exempt
def save_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("RECEIVED DATA:", data)  # <-- This will print the payload in your terminal
            
            layout = RoomLayout.objects.create(
                name=data.get('name', 'Custom Room'),
                wall_color=str(data.get('wall_color', '0xfaf9f6')),
                floor_color=str(data.get('floor_color', '0xe3d3c3')),
                furniture_data=data.get('furniture_data', [])
            )
            return JsonResponse({'status': 'success', 'layout_id': layout.id})
        except Exception as e:
            print("SAVE ERROR:", str(e))  # <-- This will print the exact python error in your terminal
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'invalid method'}, status=405)

def load_room(request, layout_id):
    try:
        layout = RoomLayout.objects.get(id=layout_id)
        data = {
            'name': layout.name,
            'wall_color': layout.wall_color,
            'floor_color': layout.floor_color,
            'furniture_data': layout.furniture_data
        }
        return JsonResponse({'status': 'success', 'layout': data})
    except RoomLayout.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Layout not found'}, status=404)