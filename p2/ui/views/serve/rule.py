"""serve rule views"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import \
    PermissionRequiredMixin as DjangoPermissionListMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, FormView, ListView, UpdateView
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from guardian.shortcuts import get_objects_for_user

from p2.lib.shortcuts import get_object_for_user_or_404
from p2.lib.views import CreateAssignPermView
from p2.serve.forms import ServeRuleDebugForm, ServeRuleForm
from p2.serve.models import ServeRule
from p2.serve.views import ServeView


class ServeRuleListView(PermissionListMixin, LoginRequiredMixin, ListView):
    """List all serve rules the user has access to"""

    model = ServeRule
    permission_required = 'p2_serve.view_serverule'
    ordering = 'name'
    paginate_by = 10


class ServeRuleCreateView(SuccessMessageMixin, DjangoPermissionListMixin, CreateAssignPermView):
    """Create new serve rule"""

    model = ServeRule
    form_class = ServeRuleForm
    permission_required = 'p2_serve.add_serverule'
    template_name = 'generic/form.html'
    success_message = _('Successfully created Rule')
    permissions = [
        'p2_serve.view_serverule',
        'p2_serve.change_serverule',
        'p2_serve.delete_serverule',
    ]

    def get_success_url(self):
        return reverse('p2_ui:serve-rule-list')


class ServeRuleUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    """Update existing serve rule"""

    model = ServeRule
    form_class = ServeRuleForm
    permission_required = 'p2_serve.change_serverule'
    template_name = 'generic/form.html'
    success_message = _('Successfully updated Rule')

    def get_success_url(self):
        return reverse('p2_ui:serve-rule-list')


class ServeRuleDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    """Delete serve rule"""

    model = ServeRule
    permission_required = 'p2_serve.delete_serverule'
    template_name = 'generic/delete.html'
    success_message = _('Successfully deleted Rule')

    def get_success_url(self):
        return reverse('p2_ui:serve-rule-list')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)


class ServeRuleDebugView(PermissionRequiredMixin, FormView):
    """Debug ServeRule"""

    form_class = ServeRuleDebugForm
    permission_required = 'p2_serve.change_serverule'
    template_name = 'generic/form.html'
    model = ServeRule

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['title'] = "Debugging Rule '%s'" % self.get_object().name
        return kwargs

    def get_object(self):
        """Get ServeRule instance"""
        return get_object_for_user_or_404(self.request.user,
                                          'p2_serve.change_serverule', pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('p2_ui:serve-rule-debug', kwargs={
            'pk': self.get_object().pk
        })

    def form_valid(self, form):
        lookup, messages = ServeView(request=self.request).rule_lookup(self.get_object())
        blob = get_objects_for_user(self.request.user, 'p2_core.view_blob').filter(**lookup)
        messages.append("Found object %r" % blob)
        form = ServeRuleDebugForm(
            data={
                'path': form.cleaned_data.get('path'),
                'result': '\n'.join(messages)
            }
        )
        return self.form_invalid(form)
