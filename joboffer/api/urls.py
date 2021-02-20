from django.urls import path

from joboffer.api.views import JobsListCreateAPIView, JobsDetailsCreateAPIView

urlpatterns = [
    path("jobs/", JobsListCreateAPIView.as_view(), name="jobs-list"),
    path("jobs/<int:pk>", JobsDetailsCreateAPIView.as_view(), name="detail-list")
]
