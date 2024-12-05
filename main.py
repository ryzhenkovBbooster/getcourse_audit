import time

import requests
import json

from getcourse_file import read_file
from googleDirectory import get_users


unique_emails = ['bbooster@unoia.ru', 'ceo@unoia.ru', 'melena@visotsky.com', 'nn.nyc@visotsky.org', 'alex@visotsky.org', 'alex@visotsky.com', 'bbmoder@bbooster.online', 'sms.getcourse.bbooster@gmail.com', 'videoupload@bbooster.online', 'content.cc@visotsky.org', 'ariel@hcatwn.com', 'demo@test.com', 'jason@hcatwn.com', 'e.shapovalyants_7@bbooster.io', 'e.shapovalyants_10@bbooster.io', 'e.shapovalyants_8@bbooster.io', 'e.shapovalyants_9@bbooster.io', 'e.shapovalyants_12@bbooster.io', 'e.shapovalyants_11@bbooster.io', ]

TOKEN = 'GvIYXkNdeBLqLywbjicrDOd6tfyYm8bjDlHjRbXm1tGZu9rJrjznjMl1RWUiBfDr2zdZGEErdYjDvqLrHC146urC45NhR8MCmJoTr7vQ6sfJQNMF4bd0oLGQ3Zf4KP9r'


def create_export():

    query = 'c%5Bsegment_id%5D=0&uc%5Brule_string%5D=%7B%22type%22%3A%22andrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22mode%22%3A%22and%22%2C%22children%22%3A%5B%7B%22type%22%3A%22andrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22mode%22%3A%22or%22%2C%22children%22%3A%5B%7B%22type%22%3A%22user_typerule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22admin%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%2C%7B%22type%22%3A%22user_typerule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22teacher%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%5D%7D%7D%2C%7B%22type%22%3A%22andrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22mode%22%3A%22or%22%2C%22children%22%3A%5B%7B%22type%22%3A%22user_statusrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22active%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%2C%7B%22type%22%3A%22user_statusrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22banned%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%5D%7D%7D%5D%7D%2C%22maxSize%22%3A%22%22%7D&formParams%5Bclarity_uid%5D=K8GiN0To7cf6ILReoqld1wLkU9Ze22a0'

    url = f"https://my.bbooster.online/pl/api/account/users?key={TOKEN}&type=admin"

    response = requests.get(url)
    data = json.loads(response.content)
    if data['error_message']:
        error_message = response.content.decode('utf-8')
        print(error_message)
        return False

    status_export = data['info']['export_id']
    return status_export

def load_export(export_id):
    while True:

        url = f'https://my.bbooster.online/pl/api/account/exports/{export_id}?key={TOKEN}'

        response = requests.get(url)
        response = json.loads(response.content)
        print(response)
        if response['success'] == False:
            time.sleep(10)
            continue


        else:


            return response
def check_mails(google_users:list, file_users: list):
    res = []
    not_found = [email for email in file_users if not any(email in sublist for sublist in google_users)]
    multiple_matches = []
    for sublist in google_users:
        matches = [email for email in file_users if email in sublist and email]

        if len(matches) > 1:
            print(matches)
            multiple_matches.extend(matches)


    return not_found


def main():
    google_users: list[list] = get_users()
    file_users:list[dict] = read_file()
    res = check_mails(google_users=google_users, file_users=file_users)




    # print(google_users)
    for i in res:
        if i not in unique_emails:
            print(i)

if __name__ == "__main__":
    main()