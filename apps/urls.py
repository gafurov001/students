from django.urls import path
from django.views.generic import TemplateView

from apps.views import UserView, CreateStudentView, DetailStudentView, UpdateStudentView, TeachersListView, \
    TeacherUpdateView, TeacherCreateView, TeacherDetailView, CustomLoginView, CustomRegisterView, LogoutView, \
    VerifyEmailConfirm

urlpatterns = [
    path('verify-email-confirm/<uidb64>/<token>', VerifyEmailConfirm.as_view(), name='verify-email-confirm'),

    path('', TeachersListView.as_view(), name='home'),
    path('teachers/', TeachersListView.as_view(), name='teachers-list'),
    path('teacher-update/<int:pk>', TeacherUpdateView.as_view(), name='teacher-update'),
    path('add-teacher/', TeacherCreateView.as_view(), name='add-teacher'),
    path('teacher-detail/<int:pk>', TeacherDetailView.as_view(), name='teacher-detail'),

    path('students/', UserView.as_view(), name='students-list'),
    path('add-student/', CreateStudentView.as_view(), name='add-student'),
    path('student-detail/<int:pk>', DetailStudentView.as_view(), name='detail-page'),
    path('student-update/<int:pk>', UpdateStudentView.as_view(), name='update-page'),

    path('login/', CustomLoginView.as_view(), name='login-page'),
    path('register/', CustomRegisterView.as_view(), name='register-page'),
    path('logout', LogoutView.as_view(), name='logout'),
]
