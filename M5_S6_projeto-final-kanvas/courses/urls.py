from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.ListCreateCourseView.as_view()),
    path("courses/<uuid:course_id>/", views.RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<uuid:course_id>/students/", views.PutStudentToCourse.as_view()),
]
