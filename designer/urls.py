from django.urls import path
from . import views

urlpatterns = [
    path('', views.canvas_view, name='canvas'),
    path('api/save/', views.save_room, name='save_room'),
    path('api/load/<int:layout_id>/', views.load_room, name='load_room'),
]