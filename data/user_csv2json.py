import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('user_data.csv', header=0,
                     names=['firstName', 'lastName', 'sex', 'email', 'role', 'username', 'password'])

    # export to array of jsons
    df.to_json('create_user_requests.json', orient='records')
