from django.conf.urls import url

from analytics.views import *

urlpatterns = [
    url(r'^', analytics_index_view, name='analytics_index'),
]