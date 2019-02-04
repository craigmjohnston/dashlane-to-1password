# parse args
import argparse
parser = argparse.ArgumentParser(description='Convert exported JSON data from Dashlane into 1Password-compatible CSV data.')
parser.add_argument('input', metavar='i', type=argparse.FileType('r'))
parser.add_argument("--output", metavar='o', type=argparse.FileType('wb'), default='output.csv', required=False)

args = parser.parse_args()

# read input json
import json
login_details = json.load(args.input)['AUTHENTIFIANT']

# output csv
import csv
writer = csv.writer(args.output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for login in login_details:
    row = [
        login['title'],
        login['domain'],
        login['login'] if login['login'] else login['email'],
        login['password'],
        login['note']
    ]

    writer.writerow(row)
