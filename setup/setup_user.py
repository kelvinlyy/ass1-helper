import json
from agents.admin_agent import AdminAgent


def create_users():
    with open('../data/create_user.json', 'rb') as f:
        create_user_requests = json.load(f)

    admin_agent = AdminAgent()

    kc_ids = []
    for request in create_user_requests:
        kc_id = admin_agent.create_keycloak_user(request)['kc_id']
        kc_ids.append(kc_id)

    with open('../data/user_kc_id.txt', 'w') as f:
        for kc_id in kc_ids:
            f.write(f'{kc_id}\n')


if __name__ == "__main__":
    create_users()
