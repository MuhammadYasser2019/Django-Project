from asyncio.log import logger

from .models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import pdb
from .Serializer import UserSerializer

import logging
# Create your views here.


@csrf_exempt
def signup(request):
    # print("*****client")
    try:
        customer_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=customer_data)
        # user_serializer.user_type = True
        # user_serializer.available_now = False
        # user_serializer.available_today = False
        if user_serializer.is_valid():
            user_serializer.save()
        return JsonResponse(True, safe=False)
    except:
        logging.exception("message")
        return JsonResponse(False, safe=False)


@csrf_exempt
def signup_ostafandy(request):
    # print("*****ostafandy")
    try:
        #pdb.set_trace()
        customer_data = JSONParser().parse(request)
        #customer_data.user_type = False
        user_serializer = UserSerializer(data=customer_data)
        if user_serializer.is_valid():
            user_serializer.save()
        return JsonResponse(True, safe=False)
    except:
        logging.exception("message")
        return JsonResponse(False, safe=False)


def login(request, username, password):
    try:
        customer = User.objects.get(username=username, password=password)
        if customer is None:
            return JsonResponse(False, safe=False)
        else:
            return JsonResponse(True, safe=False)
    except User.DoesNotExist:
        return JsonResponse(False,safe=False)


def list_osta(request, cid=1):
    try:
        osta_list = User.objects.filter(
            available_now=True,
            user_type=False,
            craft=cid
        )
        user_serializer = UserSerializer(osta_list, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    except:
        return JsonResponse([], safe=False)


def list_osta_all(request):
    try:
        osta_list = User.objects.filter(
            user_type=False,
        )
        user_serializer = UserSerializer(osta_list, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    except:
        return JsonResponse([], safe=False)


def list_all(request):
    try:
        osta_list = User.objects.all()
        user_serializer = UserSerializer(osta_list, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    except:
        return JsonResponse([], safe=False)

def change_availability(ostaid):
    try:
        user = User.objects.get(id=ostaid)
        user.available_now = False
        user.save()
        return JsonResponse(True)
    except:
        return JsonResponse(False)


