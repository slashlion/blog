from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# verifies whether is logged. dont forget add in settings LOGIN_URL = 'login'
from .models import Entry


# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']   # con el negativo ordena los registros de ultimo a mas antiguo
    paginate_by = 3


class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entry_detail.html'


class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

