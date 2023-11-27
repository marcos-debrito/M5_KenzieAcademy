from rest_framework import generics
from courses.models import Course
from .serializers import CourseSerializer, StudentsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import AccountOwner


class ListCreateCourseView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AccountOwner]
    """ Tenho que criar uma exceçção personalizada, para que um usuario comum nao possa criar um curso
        mas ao mesmo tempo, ele pode ter acesso aos SAFE Methods.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return Course.objects.all()


class RetrieveUpdateDestroyCourseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AccountOwner]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return Course.objects.all()


class PutStudentToCourse(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AccountOwner]

    queryset = Course.objects.all()
    serializer_class = StudentsSerializer
    lookup_url_kwarg = "course_id"
