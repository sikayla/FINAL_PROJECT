
from django.contrib import admin
from django.urls import path, include
from students import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/add/', views.add_learner, name='add_learner'),
    path('about/', views.about, name='about'),
    
    path('student/<int:pk>/update/', views.update_student, name='update_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),

    path('subject/<int:pk>/update/', views.update_subject, name='update_subject'),
    path('subject/<int:pk>/delete/', views.delete_subject, name='delete_subject'),

    path('grade/<int:pk>/update/', views.update_grade, name='update_grade'),
    path('grade/<int:pk>/delete/', views.delete_grade, name='delete_grade'),
    path('grade/add/<int:subject_id>/', views.add_grade, name='add_grade'),
    path('api/', include('students.api_urls')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)