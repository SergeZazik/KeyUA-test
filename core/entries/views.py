from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, Q, Sum
from django.db.models.functions import ExtractWeek
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import FormMixin

from .forms import DateRangeForm, EntryModelForm
from .models import Entry


class EntryListView(LoginRequiredMixin, ListView, FormMixin):
    model = Entry
    template_name = 'entries/entry_list.html'
    context_object_name = 'entry_list'
    form_class = DateRangeForm
    paginate_by = 10

    def get_queryset(self):
        queryset = Entry.objects.filter(author=self.request.user)
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return queryset.filter(date__range=(form.cleaned_data['start_date'], form.cleaned_data['end_date']))
        return queryset


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/entry_create.html'
    form_class = EntryModelForm
    success_url = reverse_lazy('entries:entry-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(EntryCreateView, self).form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'entries/entry_create.html'
    form_class = EntryModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Entry, id=id_)

    def get_success_url(self):
        return reverse('entries:entry-list')

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False


class EntryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'entries/entry_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Entry, id=id_)

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'entries/entry_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Entry, id=id_)

    def get_success_url(self):
        return reverse('entries:entry-list')

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False


class EntryStatisticsView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/entry_statistic.html'
    context_object_name = 'entry_statistic'
    paginate_by = 10

    def get_queryset(self):
        year = date.today().year - 1
        queryset = Entry.objects.filter(Q(author=self.request.user) and Q(date__year=year))
        statistics = queryset.annotate(week=ExtractWeek('date')).values('week').annotate(
            total_distance=Sum('distance'), total_duration=Sum('duration'), entries_count=Count('id')).annotate(
            weekly_average_speed=Sum('distance') / Sum('duration')).order_by(ExtractWeek('date'))
        return statistics
