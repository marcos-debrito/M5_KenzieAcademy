from django.db import models
from uuid import uuid4
from django.db.models import UUIDField


class StudentsStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )
    status = models.CharField(
        choices=StudentsStatus.choices,
        default=StudentsStatus.PENDING,
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
