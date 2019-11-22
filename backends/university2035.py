from django.conf import settings
from .oauth import BaseOAuth2
import re
import time



class UNTIBackend(BaseOAuth2):

    name = 'university2035'
    ID_KEY = 'username'
    AUTHORIZATION_URL = '{}/oauth2/authorize'.format(settings.SSO_UNTI_URL)
    ACCESS_TOKEN_URL = '{}/oauth2/access_token'.format(settings.SSO_UNTI_URL)
    USER_DATA_URL = '{url}/oauth2/access_token/{access_token}/'
    DEFAULT_SCOPE = []
    REDIRECT_STATE = False
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [('access_token', 'access_token'),
                  ('refresh_token', 'refresh_token'),
                  ('expires_in', 'expires_in'), #seconds to expiration
                  ('expires', 'expires'), #expiration timestamp in UTC
                  ('unti_id', 'unti_id')]


    skip_email_verification = True

    def get_user_details(self, response):
        username = response.get('username')
        email = response.get('email', '')
        if not username and email:
            username = email.split('@')[0]

        full_name, first_name, last_name = self.get_user_names(
            first_name = response.get('firstname', ''),
            last_name = response.get('lastname', '')
        )

        return {
             'username': username,
             'email': email,
             'first_name': first_name,
             'last_name': last_name,
             'fullname': full_name
        }

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(
            '{}/users/me'.format(settings.SSO_UNTI_URL),
            params={'access_token': access_token},
            headers={'Authorization': 'Bearer {}'.format(access_token)},
        )

    def add_extra(self, data):
        data['expires'] = int(time.time()) + int(data['expires_in'])
        data['access_token'] = data['access_token']
        data['refresh_token'] = data['refresh_token']
        data['unti_id'] = data['unti_id']
        return data

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        data = BaseOAuth2.extra_data(self, user, uid, response,
                                     details=details,
                                     *args, **kwargs)
        return self.add_extra(data)
