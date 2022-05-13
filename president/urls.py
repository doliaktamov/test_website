from django.urls import URLPattern, path, include
from django.contrib import admin
from qwe import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('question', views.QuestionViewSet, basename='question')
router.register('answer', views.AnswerViewSet, basename='answer')
router.register('category', views.CategoryViewSet, basename='category')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', views.AdminCreateAPIView.as_view()),
    path('result/', views.ResultCreateAPIView.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('register/', views.UserCreateAPIView.as_view()),
    path('get-token/', obtain_auth_token),
    path('', include(router.urls)),
]