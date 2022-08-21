import json
from agents.admin_agent import AdminAgent
import pandas as pd


def create_users():
    # load user data from csv
    user_df = pd.read_csv('../data/user_data.csv', header=0,
                          names=['firstName', 'lastName', 'sex', 'email', 'role', 'username', 'password'])
    create_user_dto = json.loads(user_df.to_json(orient='records'))

    admin_agent = AdminAgent()

    # create keycloak user
    # record the responded keycloak id
    kc_ids = []
    for user_request in create_user_dto:
        kc_id = admin_agent.create_keycloak_user(user_request)['kc_id']
        kc_ids.append(kc_id)

    # save the recorded keycloak ids to a txt file
    with open('../data/user_kc_id.txt', 'w') as f:
        for kc_id in kc_ids:
            f.write(f'{kc_id}\n')


if __name__ == "__main__":
    create_users()
