import csv


def read_file():

    datafile = []

    with open('user_export_2024-10-04_02-22-32.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        data  = [row for row in reader]

    for row in data:
        emailfile = row['Email']
        datafile.append(emailfile)
    return  datafile


# сотрудник активен ::
# https://my.bbooster.online/pl/user/user/index?uc%5Bsegment_id%5D=0&uc%5Brule_string%5D=%7B%22type%22%3A%22andrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22mode%22%3A%22and%22%2C%22children%22%3A%5B%7B%22type%22%3A%22user_typerule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22teacher%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%2C%7B%22type%22%3A%22user_statusrule%22%2C%22inverted%22%3A0%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22active%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%5D%7D%2C%22maxSize%22%3A%22%22%7D&formParams%5Bclarity_uid%5D=tSQJeetuKbP355G0D0oUlYJv11bPRras

# админ активен :: https://my.bbooster.online/pl/user/user/index?uc%5Bsegment_id%5D=0&uc%5Brule_string%5D=%7B%22type%22%3A%22andrule%22%2C%22inverted%22%3A0%2C%22className%22%3A%22app%3A%3Acomponents%3A%3Alogic%3A%3Arule%3A%3AAndRule%22%2C%22params%22%3A%7B%22children%22%3A%5B%7B%22type%22%3A%22user_statusrule%22%2C%22inverted%22%3A0%2C%22className%22%3A%22app%3A%3Acomponents%3A%3Alogic%3A%3Arule%3A%3ACustomFieldRule%22%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22active%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%2C%7B%22type%22%3A%22user_typerule%22%2C%22inverted%22%3A0%2C%22className%22%3A%22app%3A%3Acomponents%3A%3Alogic%3A%3Arule%3A%3ACustomFieldRule%22%2C%22params%22%3A%7B%22value%22%3A%7B%22selected_id%22%3A%5B%22admin%22%5D%7D%2C%22valueMode%22%3Anull%7D%7D%5D%2C%22mode%22%3A%22and%22%7D%7D&formParams%5Bclarity_uid%5D=tSQJeetuKbP355G0D0oUlYJv11bPRras