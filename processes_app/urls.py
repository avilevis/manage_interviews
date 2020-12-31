from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from processes_app import views

router = DefaultRouter()
router.register('', views.ProcessViewSet)

urlpatterns = [
    path('<int:pk>/', views.ProcessViewSet.as_view(
        actions={
            'get': 'list',
            'patch': 'update',
            'delete': 'destroy'
        }
    )),
    path('', include(router.urls))
]
