import os
import re

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from django.contrib.auth.models import User

import pinax

from emailconfirmation.models import EmailAddress, EmailConfirmation
#from account.utils import get_default_redirect

class LoginTest(TestCase):
    # tests based on django.contrib.auth tests
    
    urls = "account.tests.account_urls"
    
    def setUp(self):
#        self.old_installed_apps = settings.INSTALLED_APPS
#        # remove django-mailer to properly test for outbound e-mail
#        if "mailer" in settings.INSTALLED_APPS:
#            settings.INSTALLED_APPS.remove("mailer")
        pass
    
    def tearDown(self):
        pass
#        settings.INSTALLED_APPS = self.old_installed_apps
    
    def context_lookup(self, response, key):
        # used for debugging
        for subcontext in response.context:
            if key in subcontext:
                return subcontext[key]
        raise KeyError
    
    def test_login_view(self):
        """
        Test GET on /login/
        """
        response = self.client.get(reverse("acct_login"))
        self.assertEqual(response.status_code, 200)

    def test_login_default_redirect(self):
        """
        Test POST on /login/ with a correct username/password
        """
        bob = User.objects.create_user("bob", "bob@example.com", "abc123")
        data = {
            "username": "bob",
            "password": "abc123", 
            "remember": "1", 
        }
        response = self.client.post(reverse("acct_login"), data)
        success_url = reverse("after_login")
        self.assertRedirects(response, success_url)


    """
    Note: the following are not unit-tested here:
    - invalid username/password (see django.contrib.auth tests)
    - non-existent user (see django.contrib.auth tests)
    - openid (see django-openid tests)
    """
