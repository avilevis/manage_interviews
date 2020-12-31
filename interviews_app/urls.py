from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from interviews_app import views
from processes_app import views as processes_views

router = DefaultRouter()
router.register('', views.InterviewsViewSet)

urlpatterns = [
    url(r"^create/$", views.AddInterviewFormView.as_view(), name="form"),
    path('<int:company_id>/process/', processes_views.ProcessViewSet.as_view(
        actions={
            'get': 'list'
        }
    )),
    path('<int:company_id>/process/create/', processes_views.AddProcessFormView.as_view()),
    path('<int:company_id>/process/<int:process_id>/', processes_views.ProcessViewSet.as_view(
        actions={
            'get': 'retrieve',
        }
    )),
    path('', include(router.urls)),
]
