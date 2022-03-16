from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('song/',views.index, name='song'),
    path('list/<video_id>/',views.listV, name='tolist'),
    path('songs/',views.song_view, name = 'songs')
]