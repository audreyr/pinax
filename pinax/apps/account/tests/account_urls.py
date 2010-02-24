from django.conf.urls.defaults import *

from pinax.views import noop


urlpatterns = patterns("",
    url(r'^account/', include('account.urls')),
    url(r"^after_login/$", noop, name="after_login"),
    url(r"^login_openid_test/$", "account.views.login", {"associate_openid": True},
        name="login_openid_test"),
    url(r"^after_login_openid_test/$", noop, name="after_login_openid_test"),
)
