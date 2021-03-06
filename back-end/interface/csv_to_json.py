import csv, json, sys, os 

def parse_csv(csv_file):

    csvfile = open(csv_file, 'r')
    json_file = csv_file[0:((len(csv_file) -4))] + ".json"
    jsonfile = open(json_file, 'w')

    fieldnames = ("name", "status", "city", "state", "phone", "email", "years_of_service", "jacket", "jacket_size", "team_captain")
    reader = csv.DictReader(csvfile, fieldnames)

    jsonfile.write('[\n')
    count = 0

    for row in reader:
        if count != 0:
            if count != 1:
                jsonfile.write(',\n')
            jsonfile.write('{')
            jsonfile.write('\"fields\": \n')
            json.dump(row, jsonfile)
            jsonfile.write('\n')
            jsonfile.write('}')
        count += 1
    jsonfile.write('\n]')

    jsonfile.close()

