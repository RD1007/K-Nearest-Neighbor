import csv

# https://realpython.com/knn-python/

def csvReader(file, new_values):
    output_dict = dict()
    fields = (new_values.keys())
    with open(file) as fin:
        reader = csv.DictReader(fin)
        for i, row in enumerate(reader, start=1):
            temp = 0
            for field in fields:
                if row[field] == new_values[field]:
                    temp += 1
            output_dict[i] = temp
    return output_dict

def csvLength(file):
    return(len(list(csv.reader(open(file))))-1)

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
        

def validateK(csv_length, k):
    if (k > csv_length):
        print(f"k with the value of {k} is larger than the csv length of {csv_length}")
        return (False)
    if (k%2) == 0:
        print (f"k with the value of {k} is not odd")
        return (False)
    return (True)

def maxKey(max_value, output_dict, k):
    max_keys = []
    max_value += 1
    while (len(max_keys) < k):
        max_value -= 1
        for key, value in output_dict.items():
            if value == max_value:
                max_keys.append(key)
            if len(max_keys) >= k: return (max_keys)

def maxValue(output_dict):
    return (max(output_dict.values()))


def emptyIndex(file, empty_value):
    with open(file) as fin:
        reader = csv.DictReader(fin)
        return (reader.fieldnames.index(empty_value))

def mostCommon(max_keys, file, empty_index):
    common_dict = dict()
    for row_number in max_keys:
        with open(file) as fin:
            reader = csv.reader(fin)
            rows = list(reader)
            if (rows[row_number][empty_index]) in common_dict.keys():
                common_dict[rows[row_number][empty_index]] += 1
            else:
                common_dict[rows[row_number][empty_index]] = 1
    largest_value = maxValue(common_dict)
    common_dict = {key: value for key, value in common_dict.items() if value == largest_value}
    return (list(common_dict.keys()))

def display(most_likely_value, empty_value):
    if len(most_likely_value) > 1:
        print(f"{empty_value} of the input is equally likely to be the following values", *most_likely_value, sep='\n')
    else:
        print(f"{empty_value} of the input is most likely \n{most_likely_value[0]}")

# Takes user input and file and then outputs most likely response
def predicition(k, empty_value, new_values, file):
    
    output_dict = dict(csvReader(file, new_values))

    # Next 4 variables are only used once but merging the lines heavily decreases readibility
    empty_index = emptyIndex(file, empty_value)
    max_value = maxValue(output_dict)
    max_keys = maxKey(max_value, output_dict, k)

    most_likely_value = mostCommon(max_keys, file, empty_index)

    display(most_likely_value, empty_value)


def main():
    path = "inputData\\"
    file = "Popular_Baby_Names.csv"
    file = path+file
    inputs = userInputs(file)

    predicition(int(inputs[0]), inputs[1], inputs[2], file)

if __name__ == '__main__':
    main()
