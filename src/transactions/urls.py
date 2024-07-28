
from django.urls import re_path as url, include

from .views import deposit_view, withdrawal_view


app_name = 'transactions'

urlpatterns = [
    # url(r'^$', home_view, name='home'),
    url(r'^deposit/$', deposit_view, name='deposit'),
    url(r'^withdrawal/$', withdrawal_view, name='withdrawal'),
]
