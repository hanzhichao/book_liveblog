from django.conf.urls import include, url
from django.contrib import admin

from liveupdate.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ObjectList.as_view()),
    url(r'^update-after/(?P<id>\d+)/$', update_after)
]
