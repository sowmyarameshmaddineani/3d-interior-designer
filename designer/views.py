from django.shortcuts import render

def room_canvas(request):
    return render(request, 'designer/canvas.html')