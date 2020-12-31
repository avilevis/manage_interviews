from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from agents_app import views

router = DefaultRouter()
router.register('', views.AgentsViewSet)

app_name = 'agents_app'

urlpatterns = [
    url(r'^add/$', views.AddAgentFormView.as_view(), name='form'),
    path('', include(router.urls)),
]
