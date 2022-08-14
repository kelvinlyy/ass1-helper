import keycloak
import requests
from config.url_path import JOB_URL
import json


class JobAgent:
    def __init__(self):
        self.keycloak_openid = keycloak.KeycloakOpenID(server_url="http://localhost:8443",
                                                       client_id="springboot-keycloak",
                                                       realm_name="spring_test",
                                                       client_secret_key="psmMau8oEVq42NZtsArwKwDGdJws9q1J")

    def create_job(self, manager_username, manager_password, create_job_request):
        access_token = self.keycloak_openid.token(manager_username, manager_password)['access_token']
        r = requests.post(JOB_URL,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(access_token)},
                          json=create_job_request)

        return json.loads(r.content.decode('utf-8'))
