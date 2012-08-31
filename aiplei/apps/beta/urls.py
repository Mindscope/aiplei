from django.conf.urls.defaults import patterns, url

from beta.views import BetaInviteRequestFormView, BetaInviteThankView

urlpatterns = patterns('',
    url(r'^$', BetaInviteRequestFormView.as_view(), name='beta'),
    url(r'^thanks/$', BetaInviteThankView.as_view(), name='beta_thanks'),
)
