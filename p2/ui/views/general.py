"""p2 UI Index view"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.views.generic import ListView, TemplateView
from guardian.shortcuts import get_objects_for_user

from p2.core.models import Blob
from p2.ui.constants import CACHE_KEY_BLOB_COUNT


class IndexView(LoginRequiredMixin, TemplateView):
    """Show overview of volumes"""

    template_name = 'general/index.html'

    def get_blob_count(self):
        """Get cached Blob Count"""
        if not cache.get(CACHE_KEY_BLOB_COUNT, None):
            count = len(Blob.objects.all())
            cache.set(CACHE_KEY_BLOB_COUNT, count, 30)
        return cache.get(CACHE_KEY_BLOB_COUNT)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['count'] = self.get_blob_count()
        data['volumes'] = get_objects_for_user(self.request.user, 'p2_core.view_volume')
        return data

class SearchView(LoginRequiredMixin, ListView):
    """Search Blobs by their key"""

    model = Blob
    ordering = 'path'
    template_name = 'search/results.html'

    def get_queryset(self):
        return get_objects_for_user(self.request.user, 'p2_core.view_blob').filter(
            path__icontains=self.request.GET.get('q', '')).order_by(self.ordering)
