from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import FormView
from django.views.generic import ListView, DetailView, TemplateView
from tagging.views import TaggedObjectList

from core.views import OwnerRequiredMixin
from .forms import SupportSearchForm
from .models import Support


# --- TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


# --- ListView
class SupportLV(ListView):
    model = Support
    template_name = 'support/support_all.html'
    context_object_name = 'supports'
    paginate_by = 3


class SupportTOL(TaggedObjectList):
    model = Support
    template_name = 'tagging/tagging_support_list.html'


# --- DetailView
class SupportDV(DetailView):
    model = Support


# --- PDF View
class SupportPV(DetailView):
    model = Support
    template_name = 'support/support_pdf_viewer.html'


# --- FormView
class SearchFormView(FormView):
    form_class = SupportSearchForm
    template_name = 'support/support_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        support_list = Support.objects.filter(
            Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = support_list

        return render(self.request, self.template_name, context)


# --- Bootstrap Search Result
class BstrapSearchLV(ListView):
    template_name = 'support/support_bstrap_search.html'

    def get_queryset(self):
        schWord = '%s' % self.request.GET['search']
        support_list = Support.objects.filter(
            Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        self.search_term = schWord
        self.count = support_list.count()
        return support_list

    def get_context_data(self, **kwargs):
        context = super(BstrapSearchLV, self).get_context_data(**kwargs)
        context['search_term'] = self.search_term
        context['search_count'] = self.count
        return context


class SupportCreateView(LoginRequiredMixin, CreateView):
    model = Support
    fields = ['title', 'slug', 'description', 'content', 'tag', 'file']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('support:index')

    def form_invalid(self, form):
        return super(SupportCreateView, self).form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(SupportCreateView, self).form_valid(form)


class SupportChangeLV(LoginRequiredMixin, ListView):
    template_name = 'support/support_change_list.html'

    def get_queryset(self):
        return Support.objects.filter(owner=self.request.user)


class SupportUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Support
    fields = ['title', 'slug', 'description', 'content', 'tag', 'file']
    success_url = reverse_lazy('support:index')


class SupportDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Support
    success_url = reverse_lazy('support:index')
