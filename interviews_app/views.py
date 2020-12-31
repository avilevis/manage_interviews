import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from .forms import InterviewForm
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Interview
from agents_app.models import PlacementCompanyAgents
from .serializers import InterviewSerializer
from rest_framework import status
from rest_framework.response import Response


class InterviewsViewSet(viewsets.ModelViewSet):
    """View set for getting interview process"""
    authentication_classes = ()
    permission_classes = ()
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
    
    def list(self, request, *args, **kwargs):
        exclude = request.GET.get('exclude')
        self.queryset = self.queryset.order_by('-date', '-status', )
        if exclude:
            self.queryset = self.queryset.exclude(status=exclude)
        serializer = self.get_serializer(self.queryset, many=True)
        results = map(self.formatting_interview, serializer.data)
        context = {
            'status_choices': Interview.STATUS_CHOICES,
            'interviews': results,
            'form': Interview._meta.fields,
        }
        return render(request, 'interviews.html', context)

    def retrieve(self, request, *args, **kwargs):
        initial = get_object_or_404(Interview, id=kwargs['pk']).__dict__
        form = InterviewForm(initial=initial)
        if form.is_valid():
            form.save()
            return redirect('next_view')

        return render(request, 'form.html', {
            'form': form,
            'header': 'Edit Interview',
            'method': 'PATCH',
            'form_url': '',
        })

    @staticmethod
    def formatting_interview(interview):
        interview = dict(interview)
        technology_list = []
        for tech in interview['technology']:
            technology_list.append([tech_dict[1] for tech_dict in Interview.TECHNOLOGY_CHOICES if tech_dict[0] == tech][0])
        interview['technology'] = technology_list
        for status in Interview.STATUS_CHOICES:
            if status[0] == interview['status']:
                interview['status'] = status[1]
                break
        for type_ in Interview.COMPANY_TYPE_CHOICES:
            if type_[0] == interview['company_type']:
                interview['company_type'] = type_[1]
                break
        return interview


class AddInterviewFormView(FormView):
    template_name = "form.html"
    form_class = InterviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'New Interview'
        context['method'] = 'POST'
        context['form_url'] = '../'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['date'] = datetime.date.today()
        return kwargs
