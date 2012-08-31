from django.views.generic import TemplateView


class ProfileMainView(TemplateView):
    template_name = 'profiles/profile_main.html'
