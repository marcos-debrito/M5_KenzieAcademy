from rest_framework.views import APIView, status, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from movies.permissions import MoviesPermission
from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies_orders.serializers import MovieOrderSerializer
from rest_framework.permissions import (
    IsAuthenticated,
)


class MovieOrdersDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
