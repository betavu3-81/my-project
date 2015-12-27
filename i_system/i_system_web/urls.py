from django.conf.urls import patterns, include, url



from . import views



urlpatterns = patterns('',
     url(r'^1', views.ListDepartsView.as_view(),
        name ='departs-list',),

     url(r'^2', views.CreateDepartsView.as_view(),
        name='departs-new',),
)

