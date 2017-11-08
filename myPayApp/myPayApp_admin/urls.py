from django.conf.urls import url
from . import views as admin_views

urlpatterns = [
    url(r'^login/$', admin_views.login_admin, name='login'),
    url(r'^logout/$', admin_views.logout_admin, name='logout'),
    url(r'^dashboard/$', admin_views.dashboard, name="dashboard"),
    url(r'^register-user/$', admin_views.register_user, name="register-user"),
    url(r'^register-biller/$', admin_views.register_biller,
        name="register-biller")
]