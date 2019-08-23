from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightList.as_view()),
    path('<int:pk>/', views.FlightDetail.as_view()),
    path('seats', views.SeatList.as_view()),
    path('seats/<int:pk>/', views.SeatDetail.as_view()),
    path('passengers', views.PassengerList.as_view()),
    path('passengers/<int:pk>/', views.PassengerDetail.as_view()),
    path('players', views.PlayerList.as_view()),
    path('players/<int:pk>/', views.PlayerDetail.as_view()),
    path('cells', views.PassengerList.as_view()),
    path('cells/<int:pk>/', views.PassengerDetail.as_view())
]