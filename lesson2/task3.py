import csv
import random
import string

def hide_email(email):
    local_part, domain = email.split('@')
    random_local_part = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
    return f"{random_local_part}@{domain}"

def process_row(row):
    anonymized_row = []
    for item in row:
        if '@' in item:
            anonymized_item = hide_email(item)
        else:
            anonymized_item = item
        anonymized_row.append(anonymized_item)
    return anonymized_row

def hide_data(input_file, output_file):
    with open(input_file, 'r') as input_csv:
        with open(output_file, 'w', newline='') as output_csv:
            csv_reader = csv.reader(input_csv, delimiter=';')
            csv_writer = csv.writer(output_csv, delimiter=';')
            for row in csv_reader:
                anonymized_row = process_row(row)
                csv_writer.writerow(anonymized_row)

# Example usage
input_file = 'resourses/task3_resourse_files/departament.csv'
output_file = 'resourses/task3_resourse_files/departament_hidden.csv'
hide_data(input_file, output_file)
