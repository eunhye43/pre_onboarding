from django.urls import path
from postings.views import PostingDetailView, PostinglistView

urlpatterns = [
    path('', PostingDetailView.as_view()),
    path('/<int:posting_id>', PostingDetailView.as_view()),
    path('/list', PostinglistView.as_view())
]