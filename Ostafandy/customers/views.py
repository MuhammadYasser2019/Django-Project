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
        customer_data['user_type'] = True
        customer_data['available_now'] = False
        customer_data['available_today'] = False
        user_serializer = UserSerializer(data=customer_data)
        print(user_serializer.is_valid())
        print(user_serializer.errors)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    except:
        logging.exception("message")
        return JsonResponse(False, safe=False)


@csrf_exempt
def signup_ostafandy(request):
    # print("*****ostafandy")
    try:
        #pdb.set_trace()
        customer_data = JSONParser().parse(request)
        customer_data['user_type'] = False
        customer_data['available_now'] = True
        customer_data['available_today'] = True
        user_serializer = UserSerializer(data=customer_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    except:
        logging.exception("message")
        return JsonResponse(False, safe=False)


@csrf_exempt
def login(request):
    try:
        login_request = JSONParser().parse(request)
        print(login_request)
        customer = User.objects.get(username=login_request['username'], password=login_request['password'])
        user_serializer = UserSerializer(data=[customer], many=True)
        if customer is None:
            return JsonResponse(False, safe=False)
        else:
            print(user_serializer.is_valid())
            return JsonResponse(user_serializer.data, safe=False)
    except User.DoesNotExist:
        return JsonResponse(False, safe=False)


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


@csrf_exempt
def change_availability(request):
    try:
        login_request = JSONParser().parse(request)
        print(login_request)
        customer = User.objects.get(username=login_request['username'], user_type=False)
        if customer.available_now:
            customer.available_now = False
        else:
            customer.available_now = True
        customer.save()
        return JsonResponse(True, safe=False)
    except:
        return JsonResponse(False, safe=False)