from django.urls import path
from . views import PgsListView, PgsDetailView
from . import views


urlpatterns =[
    path('', PgsListView.as_view(), name='home'),
    path('pgs/<int:pk>', PgsDetailView.as_view(), name='pg_detail'),
    path('pgs/about', views.about, name='about'),
    path('pgs/contact', views.contact, name='contact')
]
