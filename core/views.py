from .form import UserRegisterForm
from django.urls import reverse_lazy
from django.views.defaults import permission_denied
from django.views.generic import CreateView
from django.views.generic import TemplateView


class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            # 'title': self.title,
            **(self.extra_context or {})
        })
        return context

# --- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'


# --- User Creation
class UserCreateView(PasswordContextMixin, CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('register_done')

    def form_valid(self, form):
        return super(UserCreateView, self).form_valid(form)


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


# prevent from other's update/delete
class OwnerRequiredMixin(object):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            return permission_denied(self.request,
                                     exception="Only creator of this object can update/delete the object.")
        return self.render_to_response(self.get_context_data())
