from agents.admin_agent import AdminAgent


def remove_users():
    admin_agent = AdminAgent()

    # read keycloak id from csv
    # delete the user record with the keycloak id
    with open('../data/user_kc_id.txt', 'r') as f:
        for kc_id in f:
            admin_agent.delete_keycloak_user(kc_id.strip())


if __name__ == "__main__":
    remove_users()
