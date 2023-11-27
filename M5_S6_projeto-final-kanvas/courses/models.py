from django.db import models
from uuid import uuid4
from django.db.models import UUIDField


class CourseStatus(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    status = models.CharField(
        choices=CourseStatus.choices,
        default=CourseStatus.NOT_STARTED,
        max_length=11,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
    )
    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )
