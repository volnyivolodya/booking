import action
from rest_framework import viewsets


# Create your views here.
from api.models import ApiUser, Hotel, Room, Booking
from api.serializers import UserSerializer, HotelSerializer, RoomSerializer, BookingSerializer



class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'path', 'get']
    serializer_class = UserSerializer


class HotelModelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomModelViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


from django.shortcuts import render, get_object_or_404

# Create your views here.
