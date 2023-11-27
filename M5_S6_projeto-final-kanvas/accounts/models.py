from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.db.models import UUIDField


class Account(AbstractUser):
    id = UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )
    email = models.EmailField(
        unique=True,
        max_length=100,
    )
    is_superuser = models.BooleanField(
        default=False,
    )


""" 
- Vamos fazer uma relação de 1:N com Students Courses e Course
- O lado 1 da relação estará Aqui!
- Logo, as FK (foreignKey) ficarão nas models de students_courses e courses
"""
