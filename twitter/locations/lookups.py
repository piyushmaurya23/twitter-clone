from ajax_select import register, LookupChannel

from .models import Location


@register('locations')
class LocationLookup(LookupChannel):
    model = Location

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')[:50]

    def format_item_display(self, item):
        return u"<span class='locations'>%s</span>" % item.name
