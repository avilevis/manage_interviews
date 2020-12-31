from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import FormView
from .models import PlacementCompanyAgents
from .forms import AddAgentForm
from .serializers import AgentsSerializer


class AgentsViewSet(viewsets.ModelViewSet):
    """View set for getting interview process"""
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AgentsSerializer
    queryset = PlacementCompanyAgents.objects.all().order_by('-id')


class AddAgentFormView(FormView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "New Agent"
        return context

    template_name = "form.html"
    form_class = AddAgentForm
