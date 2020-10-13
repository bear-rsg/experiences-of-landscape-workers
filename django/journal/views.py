from django.views.generic import (ListView, DetailView, TemplateView)
from . import models, serializers, xml_importer
from django.db.models import Q
from django.db.models.functions import Lower
from rest_framework.generics import (RetrieveAPIView, ListAPIView)
from django.shortcuts import (render)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ConstructionListView(ListView):
    """
    Class-based view to show the constructions list template
    """

    template_name = 'researchdata/list.html'
    model = models.Construction
    paginate_by = 13

    def get_queryset(self):
        """
        This view should apply the user-defined search criteria,
        to return a filtered selection of records in a specified order
        """

        # Search
        search_val = self.request.GET.get('search', '')
        new_queryset = models.Construction.objects.filter(
            Q(id__contains=search_val) |
            Q(construction_id__contains=search_val) |
            Q(name__contains=search_val) |
            Q(pattern__contains=search_val) |
            Q(description__contains=search_val) |
            Q(form__contains=search_val) |
            Q(meaning__contains=search_val)
        )

        # Return the final new query set, ordering by the specified order
        order = self.request.GET.get('orderby', 'id')
        # If starts with a '-' then means descending
        if order[0] == '-':
            # return in descending order (convert to lower for case insensitivity)
            return new_queryset.order_by(Lower(order[1:]).desc())
        else:
            # return in ascending order (convert to lower for case insensitivity)
            return new_queryset.order_by(Lower(order))


class ConstructionDetailView(DetailView):
    """
    Class-based view to show the constructions detail template
    """

    template_name = 'researchdata/detail.html'
    model = models.Construction

    def get_context_data(self, **kwargs):
        """
        Customise the context sent to the template,
        to pass data in addition to the model specified in self.model
        """

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add a list of IDs of constructions with a "phraseology" tag
        context['phraseologyconstructions'] = models.ConstructionTag.objects\
            .filter(text="phraseology").values_list("construction_id", flat=True)

        return context


class XMLImporterTemplateView(LoginRequiredMixin, TemplateView):
    """
    Class-based view to show the XML importer template
    Requires user to be logged in (via the Django dashboard)
    """

    login_url = '/dashboard/'
    template_name = 'researchdata/xml-importer.html'


@login_required
def XMLImporterProcessView(request):
    """
    Functional view to run the XML importer
    Show a success page if completed successfully, else show error page
    Requires user to be logged in (via the Django dashboard)
    """

    try:
        xml_importer.import_xml()
        return render(request, 'researchdata/xml-importer-success.html')

    except Exception as e:
        print(e)
        return render(request, 'researchdata/xml-importer-fail.html')


# API views


class APITemplateView(TemplateView):
    """
    Display the API template
    """
    template_name = 'researchdata/api.html'


class ConstructionListAPIView(ListAPIView):
    """
    Return list of all constructions
    """
    queryset = models.Construction.objects.all()
    serializer_class = serializers.ConstructionSerializer


class ConstructionRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific construction
    """
    queryset = models.Construction.objects.all()
    serializer_class = serializers.ConstructionSerializer
