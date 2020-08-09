from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapi1.serializers import AddTwoNumbersSerializer

@ csrf_exempt
def add_two_number(request):
    if request.method == 'GET':
        return JsonResponse({'message':'hello, this is response of get request.'})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # print('request : ', request.post)
        print('data : ', data)

        serializer = AddTwoNumbersSerializer(data = data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            # now add two numbers
            result = number1 + number2
            return JsonResponse({'The sum is ':result})
        return JsonResponse({'Error':'something went wrong'})


# creating rest api using api_view

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.decorators import renderer_classes, parser_classes

@api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
def add_two_number_rest(request):
    if request.method == 'GET':
        return Response({'message':'hello, this is response of get request from version 2'})

    elif request.method == 'POST':
        serializer = AddTwoNumbersSerializer(data = request.data)
        # if serializer.is_valid():
        #     number1 = serializer.validated_data['number1']
        #     number2 = serializer.validated_data['number2']
        #     # now add two numbers
        #     result = number1 + number2
        #     return Response({'The sum is ':result})
        # print(serializer.errors)
        # return Response(serializer.errors, status=400)

        serializer.is_valid(raise_exception=True)
        number1 = serializer.validated_data['number1']
        number2 = serializer.validated_data['number2']
        # now add two numbers
        result = number1 + number2
        return Response({'The sum is ':result})
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def info_views(request, pk=None):
    from .models import Info
    from .serializers import InfoSerializer
    if request.method == "GET":
        qs = Info.objects.all()
        # array = []
        # for i in qs:
        #     serialize = InfoSerializer(instance = i)
        #     array.append(serialize.data)
        # print(array)
        # return Response(array)
        print(qs)
        serlize = InfoSerializer(instance = qs, many = True)
        return Response(serlize.data)

    elif request.method == "POST":
        serialize = InfoSerializer(data = request.data)
        serialize.is_valid(raise_exception = True)
        # # without using serializer
        # name = serialize.validated_data['name']
        # address = serialize.validated_data['address']

        # obj = Info.objects.create(
        #     name = name,
        #     address = address
        # )

        # using serializer
        serialize.save()
        return Response({'status':'OK', 'data':serialize.data})
    
    elif request.method == 'PUT':
        try:
            obj = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'errors':'Info does not exist PUT'},status=404)
        serialize = InfoSerializer(data = request.data, instance = obj)
        serialize.is_valid(raise_exception = True)
        # # without using serializer
        # name = serialize.validated_data['name']
        # address = serialize.validated_data['address']
        # obj.name = name
        # obj.address = address
        # obj.save()

        # using serializer
        serialize.save()
        return Response({'status':'OK','data':serialize.data})

    elif request.method == 'DELETE':
        try:
            obj = Info.objects.get(pk = pk)
        except Info.DoesNotExist:
            return Response({'error': 'Info does not exist DELETE'})
        
        obj.delete()
        return Response({'status': 'OK Deleted'})