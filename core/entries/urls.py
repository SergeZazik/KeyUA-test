from django.urls import path

from .views import (EntryCreateView, EntryDeleteView, EntryDetailView,
                    EntryListView, EntryStatisticsView, EntryUpdateView)

app_name = 'entries'
urlpatterns = [
    path('', EntryListView.as_view(), name='entry-list'),
    path('entry/create/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:id>/update/', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:id>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    path('entry/<int:id>/detail/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/statistics/', EntryStatisticsView.as_view(), name='entry-statistic')
]
