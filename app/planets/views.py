from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Planet
from .serializers import PlanetSerializer


class PlanetList(APIView):
    def get(self, request, format=None):
            """
            Retrieve all the planets and return a serialized representation.

            Args:
                request: The HTTP request object.
                format: The requested format for the response data (default: None).

            Returns:
                A Response object containing the serialized representation of all the planets.
            """
            planets = Planet.objects.all()
            serializer = PlanetSerializer(planets, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
            """
            Create a new planet.

            Parameters:
            - request: The HTTP request object.
            - format: The format of the response data (default: None).

            Returns:
            - If the serializer is valid, returns a response with the serialized planet data and status code 201 (Created).
            - If the serializer is not valid, returns a response with the serializer errors and status code 400 (Bad Request).
            """
            serializer = PlanetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetDetail(APIView):
    def get_object(self, pk):
        """
        Retrieve a planet object by its primary key.

        Args:
            pk (int): The primary key of the planet.

        Returns:
            Planet: The planet object with the specified primary key.

        Raises:
            Http404: If the planet with the specified primary key does not exist.
        """
        try:
            return Planet.objects.get(pk=pk)
        except Planet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            """
            Retrieve a specific planet by its primary key.

            Args:
                request (HttpRequest): The HTTP request object.
                pk (int): The primary key of the planet to retrieve.
                format (str, optional): The desired format for the response. Defaults to None.

            Returns:
                Response: The serialized data of the retrieved planet.
            """
            planet = self.get_object(pk)
            serializer = PlanetSerializer(planet)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update an existing planet.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the planet to be updated.
            format (str, optional): The format of the response data. Defaults to None.

        Returns:
            Response: The HTTP response object containing the updated planet data or error messages.
        """
        planet = self.get_object(pk)
        serializer = PlanetSerializer(planet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deletes a planet with the given primary key.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the planet to delete.
            format (str, optional): The format of the response data. Defaults to None.

        Returns:
            Response: A response with status code 204 (No Content) indicating successful deletion.
        """
        planet = self.get_object(pk)
        planet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
