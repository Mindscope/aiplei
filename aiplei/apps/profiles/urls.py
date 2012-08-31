from django.conf.urls import patterns, include, url

from views import ProfileMainView

urlpatterns = patterns('',
        url(r'^$', ProfileMainView.as_view(), name='profile_main'),
)
