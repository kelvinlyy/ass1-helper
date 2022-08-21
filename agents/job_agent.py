import keycloak
import requests
from config.url_path import JOB_URL
import json


class JobAgent:
    def __init__(self, username, password):
        self.keycloak_openid = keycloak.KeycloakOpenID(server_url="http://localhost:8443",
                                                       client_id="springboot-keycloak",
                                                       realm_name="spring_test",
                                                       client_secret_key="psmMau8oEVq42NZtsArwKwDGdJws9q1J")

        self.access_token = self.keycloak_openid.token(username, password)['access_token']

    def create_job(self, create_job_request):
        r = requests.post(JOB_URL,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(self.access_token)},
                          json=create_job_request)

        return json.loads(r.content.decode('utf-8'))

    def get_job(self, job_id):
        r = requests.get(JOB_URL + f'/{job_id}',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)})

        return json.loads(r.content.decode('utf-8'))

    def get_jobs(self, job_ids):
        r = requests.get(JOB_URL,
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)},
                         json=job_ids)

        return json.loads(r.content.decode('utf-8'))

    def update_job(self, update_job_request):
        r = requests.put(JOB_URL,
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)},
                         json=update_job_request)

        return json.loads(r.content.decode('utf-8'))

    def delete_job(self, job_id):
        r = requests.delete(JOB_URL + f'/{job_id}',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': 'Bearer {}'.format(self.access_token)})

        return r.status_code

    def search_jobs(self, search_request):
        r = requests.get(JOB_URL + f'/search',
                         headers={'Content-Type': 'application/json',
                                  'Authorization': 'Bearer {}'.format(self.access_token)},
                         json=search_request)

        return json.loads(r.content.decode('utf-8'))


if __name__ == "__main__":
    manager_username = "kelvin"
    manager_password = "password"
    job_agent = JobAgent(username=manager_username, password=manager_password)

    print(f'Manager {manager_username} create job:')
    print(json.dumps(job_agent.create_job({
        "code": "C05-2",
        "title": "Apple-mk",
        "description": "Slice-peel",
        "workerID": 1
    }), indent=2))
    print()

    print(f'Manager {manager_username} get job:')
    print(json.dumps(job_agent.get_job(1), indent=2))
    print()

    print(f'Manager {manager_username} get jobs:')
    print(json.dumps(job_agent.get_jobs([1, 2, 3, 4]), indent=2))
    print()

    print(f'Manager {manager_username} update job:')
    print(json.dumps(job_agent.update_job({
        "id": 4,
        "code": "big change",
        "title": "Apple code",
        "description": "peel",
        "workerID": 2
    }), indent=2))
    print()

    print(f'Manager {manager_username} delete job:')
    print(job_agent.delete_job(2))
    print()

    print(f'Manager {manager_username} search job:')
    print(json.dumps(job_agent.search_jobs({
        "searchText": "h"
    }), indent=2))
