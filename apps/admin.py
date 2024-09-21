from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

import apps.models.user
from apps.models.proxies import AdminUser, StudentUser, TeacherUser, ModeratorUser
from apps.models.user import User


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=User.Type.ADMIN)

    def save_model(self, request, obj, form, change):
        obj.type = TeacherUser.Type.ADMIN
        super().save_model(request, obj, form, change)


@admin.register(StudentUser)
class StudentUserAdmin(UserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=User.Type.STUDENT)

    def save_model(self, request, obj, form, change):
        obj.type = TeacherUser.Type.STUDENT
        super().save_model(request, obj, form, change)


@admin.register(ModeratorUser)
class ModeratorUserAdmin(UserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=User.Type.MODERATOR)

    def save_model(self, request, obj, form, change):
        obj.type = TeacherUser.Type.MODERATOR
        super().save_model(request, obj, form, change)


@admin.register(TeacherUser)
class TeacherUserAdmin(UserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=User.Type.TEACHER)

    def save_model(self, request, obj, form, change):
        obj.type = TeacherUser.Type.TEACHER
        super().save_model(request, obj, form, change)


admin.site.unregister(Group)
