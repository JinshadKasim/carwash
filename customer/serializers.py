from rest_framework import serializers
from customer.models import Bookings

class BookingsRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ('id','name','email','phone','department','place')