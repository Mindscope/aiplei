"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard
from admin_tools.utils import get_admin_site_name
#from queo_admin import analytics


class QueoIndexDashboard(Dashboard):
    """
    Custom index dashboard for dashboard.
    """

    columns = 2

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('django.contrib.*',),
        ))

        self.children.append(modules.RecentActions(_('Recent Actions'), 5))

