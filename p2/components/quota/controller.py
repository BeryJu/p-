"""p2 quota controller"""

from p2.components.quota.constants import TAG_QUOTA_THRESHOLD
from p2.core.components.base import ComponentController


# pylint: disable=too-few-public-methods
class QuotaController(ComponentController):
    """Quota controller"""

    template_name = 'components/quota/card.html'
    form_class = 'p2.components.quota.forms.QuotaForm'

    # TODO: Implement core functionality

    @property
    def quota_percentage(self):
        """Check if volume is close to any quota"""
        return self.volume.space_used / (int(self.component.tags.get(TAG_QUOTA_THRESHOLD)) / 100)