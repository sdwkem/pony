from django.conf.urls import include, url, patterns
from django.contrib import admin
from views import IndexView
urlpatterns = patterns('',

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view())
)
