from django.conf.urls import include, url, patterns
from django.contrib import admin
from views import IndexView, Journal_sdachaView, DeleteJournal_sdacha, DeleteJournal_technicks, DeleteJournal_workers
from views import Journal_workersView, Journal_technicksView
urlpatterns = patterns('',

    #url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^Journal_technicks', Journal_technicksView.as_view()),
    url(r'^delete_tec', DeleteJournal_technicks.as_view()),
    url(r'^Journal_workers', Journal_workersView.as_view()),
    url(r'^delete_work', DeleteJournal_workers.as_view()),
    url(r'^Journal_sdacha', Journal_sdachaView.as_view()),
    url(r'^delete_sdacha', DeleteJournal_sdacha.as_view()),

    url(r'^$', IndexView.as_view())
)
