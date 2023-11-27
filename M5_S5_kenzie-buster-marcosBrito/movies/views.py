from rest_framework.views import APIView, status, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from .permissions import MoviesPermission
from rest_framework.pagination import PageNumberPagination

""" Relacionamento de 1:N com os movies! sendo aqui o lado N da relação :D """


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, MoviesPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        result = self.paginate_queryset(movies, request)

        serializer = MovieSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, MoviesPermission]

    def get(self, request: Request, movie_id) -> Response:
        found_movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(found_movie)
        return Response(serializer.data)

    def delete(self, request: Request, movie_id) -> Response:
        found_movie = get_object_or_404(Movie, pk=movie_id)
        found_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
