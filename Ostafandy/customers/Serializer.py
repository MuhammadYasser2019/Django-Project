from rest_framework import serializers
from customers.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'full_name',
                  'username',
                  'password',
                  'phone_number',
                  'user_type',
                  'available_now',
                  'available_today',
                  'craft',

                  )
