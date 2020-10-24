from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    """
    Class-based view to show the index template - the only template in the SPA (single-paged application)
    """
    template_name = 'clientweb/index.html'
