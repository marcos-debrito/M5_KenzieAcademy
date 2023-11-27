from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSuperUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ContentSerializer
from courses.models import Course
from contents.models import Content
from rest_framework.exceptions import NotFound

from .permissions import AccountContentOwner


class CreateContentDetailView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]

    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        return serializer.save(course_id=self.kwargs[self.lookup_url_kwarg])


class RetrieveUpdateDestroyContentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AccountContentOwner]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def get_object(self):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        content = Content.objects.filter(pk=self.kwargs["content_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        if not content:
            raise NotFound({"detail": "content not found."})

        self.check_object_permissions(self.request, content)
        return content
