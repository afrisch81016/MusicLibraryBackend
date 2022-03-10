from django.urls import path
from . import views
urlpatterns = [
    path('music',views.song_list),
    path('<int:pk>/',views.song_detail),
]