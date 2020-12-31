from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from interviews_app import views as interviews_app_view
from .models import Processes
from .forms import AddProcessForm
from .serializers import ProcessesSerializer
from rest_framework import status


class ProcessViewSet(viewsets.ModelViewSet):
    """View set for getting interview process"""
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ProcessesSerializer
    queryset = Processes.objects.all().order_by('-date', '-start_time')

    def list(self, request, *args, **kwargs):
        if "company_id" in kwargs:
            self.queryset = self.queryset.filter(company_id=kwargs['company_id'])
        elif "pk" in kwargs:
            self.queryset = self.queryset.filter(id=kwargs['pk']).first()
            serializer = ProcessesSerializer(self.queryset, many=False)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        initial = get_object_or_404(Processes, id=kwargs['process_id']).__dict__
        if kwargs['company_id']:
            initial['company'] = self.kwargs['company_id']
        form = AddProcessForm(initial=initial)
        # if form.is_valid():
        #     form.save()
        #     return redirect('next_view')

        return render(request, 'form.html', {
            'form': form,
            'header': 'Edit Process',
            'method': 'PATCH',
            'form_url': f'/api/process/{initial["id"]}/',
        })


class AddProcessFormView(FormView):
    template_name = "form.html"
    form_class = AddProcessForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "New Process"
        if 'company_id' in self.kwargs:
            context['company_id'] = self.kwargs['company_id']
            context['method'] = 'POST'
            context['form_url'] = '/api/process/'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['company'] = self.kwargs['company_id']
        return kwargs
