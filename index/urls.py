from django.conf.urls import url

from index.views import *

urlpatterns = [
    url(r'07_remark', remark_views),
    url(r'^08_userLogin/$', userLogin_views),
    url(r'^09_register/$', register_views),
    url(r'^10_login/$', loginform_views),
    url(r'^11_index/$', index_views),
    url(r'^12_widget1/$', widget1_views),
    url(r'^13_cookie1/$', cookie1_views),
    url(r'^14_cookie2/$', cookie2_views),
    url(r'^15_login/$', login15_views),
    url(r'^16_getCookie/$', getcookie_views),
]
