import pandas as pd


first_name_list = ['Ryan', 'Peter', 'Harry', 'Emily', 'Joe', 'Zoe', 'Kelvin']
last_name_list = ['Chan', 'Chan', 'Lai', 'Yau', 'Chan', 'Lee', 'Lai']
sex_list = ['Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male']
email_list = map(lambda m: m.lower() + '@test.com', first_name_list)
role_list = ['worker', 'worker', 'worker', 'worker', 'manager', 'manager', 'manager']
username_list = map(lambda u: u.lower(), first_name_list)
password_list = ['password'] * 7


if __name__ == '__main__':
    df = pd.DataFrame(
        {
            "firstName": first_name_list,
            "lastName": last_name_list,
            "sex": sex_list,
            "email": email_list,
            "role": role_list,
            "username": username_list,
            "password": password_list
        }
    )

    # export to array of jsons
    df.to_json('create_user.json', orient='records')
