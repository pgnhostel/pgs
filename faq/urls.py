from django.urls import path
from . views import FaqListView


urlpatterns = [
    path('faq/', FaqListView.as_view(), name='faq')
]
