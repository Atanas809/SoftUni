from django.urls import path

from unit_integration_testing.web.views import ProfileListView, ProfileCreateView

urlpatterns = [
    path('', ProfileListView.as_view(), name='show profiles'),
    path('create/', ProfileCreateView.as_view(), name='create profile'),
]
