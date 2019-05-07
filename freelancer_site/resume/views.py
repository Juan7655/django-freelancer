from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

# class HomePageView(LoginRequiredMixin, TemplateView):
# login_url = '/login/'
# redirect_field_name = 'redirect_to'
#   template_name = "index.html"
