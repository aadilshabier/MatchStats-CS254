from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user/account.html'