import keycloak
import requests
from config.url_path import MANAGER_URL
import json


class ManagerAgent:
    def __init__(self, manager_username, manager_password):
        self.keycloak_openid = keycloak.KeycloakOpenID(server_url="http://localhost:8443",
                                                       client_id="springboot-keycloak",
                                                       realm_name="spring_test",
                                                       client_secret_key="psmMau8oEVq42NZtsArwKwDGdJws9q1J")

        self.access_token = self.keycloak_openid.token(manager_username, manager_password)['access_token']

    def view_own(self):
        r = requests.get(MANAGER_URL,
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))

    def view_jobs(self):
        r = requests.get(MANAGER_URL + '/jobs',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))

    def view_workers(self):
        r = requests.get(MANAGER_URL + '/workers',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))


if __name__ == "__main__":
    username = 'kelvin'
    password = 'password'
    print(f'Manager {username} view own:')
    manager_agent = ManagerAgent(manager_username=username, manager_password=password)
    print(json.dumps(manager_agent.view_own(), indent=2, sort_keys=True))
    print()

    print(f'Manager {username} view jobs:')
    print(json.dumps(manager_agent.view_jobs(), indent=2, sort_keys=True))
    print()

    print(f'Manager {username} view workers:')
    print(json.dumps(manager_agent.view_workers(), indent=2, sort_keys=True))

