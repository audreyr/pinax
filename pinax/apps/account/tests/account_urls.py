from django.conf.urls.defaults import *

from pinax.views import noop


urlpatterns = patterns("",
    url(r'^account/', include('account.urls')),
    url(r"^after_login/$", noop, name="after_login"),
)
