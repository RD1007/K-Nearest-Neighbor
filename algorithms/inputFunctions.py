import csv

#Take any field that gives the exact same data as each other and then remove that
def userInputs(file):
    k = 0
    while True:
        k = int(input(f"Enter an odd numbers smaller than {csvLength(file)}: "))
        if (validateK(csvLength(file), k)):
            break
    while True:
        empty_value = (input(f"Of the following values pick a value to find \n{(csv.DictReader(open(file))).fieldnames}: "))
        if (empty_value in ((csv.DictReader(open(file))).fieldnames)):
            break


    new_values = dict()
    with open(file) as fin:
        reader = csv.DictReader(fin)
        fields = reader.fieldnames
        for field in [f for f in fields if f != empty_value]:
            new_values[field] = (input(f"Enter a value for {field}: "))
    new_values = {key: value for key, value in new_values.items() if value}

    # return [new_values]
    return [k, empty_value, new_values]


def csvLength(file):
    return(len(list(csv.reader(open(file))))-1)

def validateK(csv_length, k):
    if (k > csv_length):
        print(f"k with the value of {k} is larger than the csv length of {csv_length}")
        return (False)
    if (k%2) == 0:
        print (f"k with the value of {k} is not odd")
        return (False)
    return (True)