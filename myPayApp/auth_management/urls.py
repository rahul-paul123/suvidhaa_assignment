from django.conf.urls import url
from . import views as user_views

urlpatterns = [
    url(r'^login/$', user_views.login_user, name='user-login'),
    url(r'^logout/$', user_views.logout_user, name='user-logout'),
    url(r'^biller/dashboard/$', user_views.biller_dashboard,
        name="biller-dashboard"),
    url(r'^user/dashboard/$', user_views.user_dashboard,
        name="user-dashboard"),
    url(r'^profile/update/$', user_views.change_profile,
        name="change-profile"),
]