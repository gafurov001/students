from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, CharField, ImageField, DateField, DateTimeField, BooleanField, EmailField


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    user_id = CharField(max_length=20)
    gender = CharField(max_length=20, null=True)
    date_of_birth = DateField(blank=True, null=True)
    group = CharField(max_length=3)
    image = ImageField(upload_to='%Y/%m/%d', null=True, default='user/avatar.png')
    phone_number = CharField(max_length=25, null=True)
    type = CharField(max_length=20, choices=Type.choices, default=Type.STUDENT)
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)

    email = EmailField(unique=True)
    is_active = BooleanField(default=False)

    class Meta:
        unique_together = [
            ('email', 'is_active')
        ]

