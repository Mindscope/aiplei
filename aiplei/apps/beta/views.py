from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.conf import settings
from django.http import HttpResponseRedirect

from forms import BetaInviteRequestForm


class BetaInviteRequestFormView(FormView):
    template_name = 'beta/beta_form.html'
    form_class = BetaInviteRequestForm
    success_url = 'thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        beta_request = form.save()
        beta_request.save()
        return super(BetaInviteRequestFormView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if hasattr(settings, 'INVITE_MODE') and settings.INVITE_MODE:
            if request.user.is_authenticated():
                return HttpResponseRedirect(reverse('profile_main'))
        return super(BetaInviteRequestFormView, self).dispatch(*args, **kwargs)


class BetaInviteThankView(TemplateView):
    template_name = 'beta/beta_thanks.html'
