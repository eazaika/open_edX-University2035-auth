# open_edX-University2035-auth
Integrate authorization for hawthorn.2 throw University 2035
-
In edx-platform/lms/static/sass/views/_login-register.scss you add button-oa2-university2035:  
https://github.com/eazaika/open_edX-University2035-auth/blob/6e1fdcac6a4372ea961be4b5bddcdbd10fc4c545/static/sass/views/_login-register.scss#L656  
***
edx-platform/lms/envs/common.py and aws.py  
...  
SSO_UNTI_URL = AUTH_TOKENS.get("SSO_UNTI_URL", SSO_UNTI_URL)  
API_UNTI_URL = AUTH_TOKENS.get("API_UNTI_URL", API_UNTI_URL)  
SOCIAL_AUTH_UNIVERSITY2035_API_KEY = AUTH_TOKENS.get("SOCIAL_AUTH_UNIVERSITY2035_API_KEY", SOCIAL_AUTH_UNIVERSITY2035_API_KEY)  
SOCIAL_AUTH_UNIVERSITY2035_KEY = AUTH_TOKENS.get("SOCIAL_AUTH_UNIVERSITY2035_KEY", SOCIAL_AUTH_UNIVERSITY2035_KEY)  
SOCIAL_AUTH_UNIVERSITY2035_SECRET = AUTH_TOKENS.get("SOCIAL_AUTH_UNIVERSITY2035_SECRET", SOCIAL_AUTH_UNIVERSITY2035_SECRET)  
...  
if FEATURES.get('ENABLE_THIRD_PARTY_AUTH'):  
    tmp_backends = ENV_TOKENS.get('THIRD_PARTY_AUTH_BACKENDS', [  
        'social_core.backends.university2035.UNTIBackend',  
     
...
***
In mysql:  
select edxapp;  
update third_party_auth_oauth2providerconfig set icon_class=NULL where id=18;  
