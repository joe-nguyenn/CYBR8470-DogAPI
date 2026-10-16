from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogList(APIView):

    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):

    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dog = self.get_object(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BreedList(APIView):

    def get(self, request):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BreedSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):

    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        breed = self.get_object(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)