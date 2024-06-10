import csv

def fieldKeys(file):
    with open(file) as fin:
        reader = csv.DictReader(fin)
        return (reader.fieldnames)

def fieldOptions(file, fields):
    field_options = dict()
    for field in fields:
        field_options[field] = set()
        with open(file) as fin:
            reader = csv.DictReader(fin)

            for row in reader:
                field_options[field].add(row.get(field))
    return (field_options)

def main():
    path = "inputData\\"
    file = "Popular_Baby_Names.csv"
    file = path+file

    field_options = fieldOptions(file, fieldKeys(file))

if __name__ == '__main__':
    main()