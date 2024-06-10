import csv
from inputFunctions import userInputs

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
