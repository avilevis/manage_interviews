import json
from rest_framework.renderers import TemplateHTMLRenderer


class InterviewHtmlRenderer(TemplateHTMLRenderer):
    media_type = 'text/html'
    format = 'api'
    template_name = 'info.html'

    def get_template_context(self, data, renderer_context):
        context = {
            'header': "Details",
            'data': json.loads(json.dumps(data))
        }
        
        response = renderer_context['response']
        if response.exception:
            context['status_code'] = response.status_code
        return context
