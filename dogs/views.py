
# Create your views here.

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from dogs.serializers import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions


class Dogs(APIView):

    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogListSerializer(dogs, many=True)
        return Response({"data": serializer.data})

    def post(self, request):

        serializer = DogSerializer(data=request.data)

        if serializer.is_valid():
            try:
                Dog.objects.get(id=request.POST.get('id'))
                return Response(status=400)
            except ObjectDoesNotExist:
                serializer.save()
                return Response(status=201)
        else:
            return Response(serializer.errors, status=400)



class DogDetails(APIView):

    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=False)
        return Response({"data": serializer.data})

    def post(self, request):
        serializer = DogSerializer(data=request.data)

        if serializer.is_valid():
            try:
                Dog.objects.get(id=request.POST.get('id'))
                return Response(status=400)
            except ObjectDoesNotExist:
                serializer.save()
                return Response(status=201)
        else:
            return Response(serializer.errors, status=400)



class Kennels(APIView):

    def get(self, request):
        kennels = Kennel.objects.all()
        serializer = KennelSerializer(kennels, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Kennel.objects.create(creater=request.user)
        return Response(status=201)


class Breeds(APIView):

    def get(self, request):
        breeds = DogBreed.objects.all()
        serializer = DogBreedSerializer(breeds, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        DogBreedSerializer.objects.create(creater=request.user)
        return Response(status=201)

