import keycloak
import requests
from config.url_path import *
import json


class AdminAgent:
    def __init__(self, username='admin', password='password'):
        self.keycloak_openid = keycloak.KeycloakOpenID(server_url="http://localhost:8443",
                                                       client_id="springboot-keycloak",
                                                       realm_name="spring_test",
                                                       client_secret_key="psmMau8oEVq42NZtsArwKwDGdJws9q1J")

        self.access_token = self.keycloak_openid.token(username, password)['access_token']

    def get_keycloak_id(self):
        r = requests.get(ADMIN_URL + '/id',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return r.content.decode('utf-8')

    def create_keycloak_user(self, create_request):
        r = requests.post(ADMIN_URL,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(self.access_token)},
                          json=create_request)

        return json.loads(r.content.decode('utf-8'))

    def delete_keycloak_user(self, kc_id):
        r = requests.delete(ADMIN_URL + f'/{kc_id}',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': 'Bearer {}'.format(self.access_token)})
        return r.status_code


if __name__ == "__main__":
    admin_agent = AdminAgent()
    print(admin_agent.get_keycloak_id())
