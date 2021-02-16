# coding: utf-8

from __future__ import absolute_import, print_function
from docusign_click import AccountsApi, ApiException

import base64
import os
import unittest
import docusign_click as docusign

Username = os.environ.get("USER_NAME")
IntegratorKey = os.environ.get("INTEGRATOR_KEY_JWT")
BaseUrl = "https://demo.docusign.net/clickapi"
OauthHostName = "account-d.docusign.com"
SignTest1File = "{}/docs/SignTest1.pdf".format(os.path.dirname(os.path.abspath(__file__)))
TemplateId = os.environ.get("TEMPLATE_ID")
UserId = os.environ.get("USER_ID")
PrivateKeyBytes = base64.b64decode(os.environ.get("PRIVATE_KEY"))


class SdkUnitTests(unittest.TestCase):

    def setUp(self):
        self.api_client = docusign.ApiClient(base_path=BaseUrl, oauth_host_name=OauthHostName)
        self.api_client.rest_client.pool_manager.clear()

        docusign.configuration.api_client = self.api_client
        try:
            self.api_client.host = BaseUrl
            token = (self.api_client.request_jwt_user_token(client_id=IntegratorKey,
                                                            user_id=UserId,
                                                            oauth_host_name=OauthHostName,
                                                            private_key_bytes=PrivateKeyBytes,
                                                            expires_in=3600,
                                                            scopes=["signature", "impersonation",
                                                                     "click.manage", "click.send"]))
            self.user_info = self.api_client.get_user_info(token.access_token)
            self.api_client.rest_client.pool_manager.clear()
            docusign.configuration.api_client = self.api_client

        except ApiException as e:
            print("\nException when setting up DocuSign Click API: %s" % e)
        self.api_client.rest_client.pool_manager.clear()

    def tearDown(self):
        self.api_client.rest_client.pool_manager.clear()

    def testGetClickWraps(self):
        # Testing for the UserInfo which is true if auth is successful
        try:
            print(self.user_info)
            self.assertIsNotNone(self.user_info)
            self.assertTrue(len(self.user_info.accounts) > 0)
            self.assertIsNotNone(self.user_info.accounts[0].account_id)

            accountId = self.user_info.accounts[0].account_id
            api = AccountsApi()
            clickResponse = api.get_clickwraps(accountId)

            self.assertIsNotNone(clickResponse)
            self.assertIsNotNone(len(clickResponse.clickwraps))
            self.assertIsNotNone(clickResponse.clickwraps[0].version_id)

        except ApiException as e:
            print("\nException when setting up DocuSign Click API: %s" % e)
        self.api_client.rest_client.pool_manager.clear()


if __name__ == '__main__':
    unittest.main()
