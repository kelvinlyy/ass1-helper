import keycloak
import requests
from config.url_path import WORKER_URL
import json


class WorkerAgent:
    def __init__(self, worker_username, worker_password):
        self.keycloak_openid = keycloak.KeycloakOpenID(server_url="http://localhost:8443",
                                                       client_id="springboot-keycloak",
                                                       realm_name="spring_test",
                                                       client_secret_key="psmMau8oEVq42NZtsArwKwDGdJws9q1J")

        self.access_token = self.keycloak_openid.token(worker_username, worker_password)['access_token']

    def view_own(self):
        r = requests.get(WORKER_URL,
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))

    def view_jobs(self):
        r = requests.get(WORKER_URL + '/jobs',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))

    def complete_job(self, job_id):
        r = requests.put(WORKER_URL + f'/{job_id}',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))


if __name__ == "__main__":
    username = 'harry'
    password = 'password'
    print(f'Worker {username} view own:')
    worker_agent = WorkerAgent(worker_username=username, worker_password=password)
    print(json.dumps(worker_agent.view_own(), indent=2, sort_keys=True))
    print()

    print(f'Worker {username} view jobs:')
    print(json.dumps(worker_agent.view_jobs(), indent=2, sort_keys=True))
    print()

    print(f'Worker {username} complete job:')
    print(json.dumps(worker_agent.complete_job(2), indent=2, sort_keys=True))

