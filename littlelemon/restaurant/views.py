from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import menu, booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import viewsets, routers
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer


router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)
