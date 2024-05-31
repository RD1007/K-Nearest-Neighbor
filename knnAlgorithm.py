import math
import string
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# https://realpython.com/knn-python/

def csvReader(file):
    output_dict = dict()
    with open(file) as fin:
        dr = csv.DictReader(fin)
        for row in dr:
            output_dict[row.get('letter')] = [int(row.get('x')), int(row.get('y')), int(row.get('z'))], row.get('color')
    return output_dict

def norm(a, b):
    sideValues = 0
    for n in range(0, max(len(a),len(b))):
        sideValues += ((a[n]-b[n])**2) # Add a check for if there is no value in that position
    norm = round(math.sqrt(sideValues),2)
    return norm

def display(output_dict):
    for keys, values in output_dict.items():
        plt.scatter(values[0][0], values[0][1], values[0][2], values[1])
        plt.text(x=values[0][0]-0.5, y=values[0][1]-0.5, s=f"{keys}")
    plt.title("3D Plane")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def distance(input_dict, new_point):
    distance_dict = dict()
    values_set = set()
    for keys, values in input_dict.items():
        distance = float(norm(values[0], new_point))
        distance_dict[keys] = distance
        values_set.add(distance)
    return closest(distance_dict, values_set)

def closest(distance_dict, values_set):
    distance_dict = dict(distance_dict)
    values_set = set(values_set)
    new_dict = dict()
    for i in range(3):
        for keys, values in distance_dict.items():
            if values == min(values_set):
                new_dict[keys] = values
                # distance_dict.pop(keys)
        values_set.remove(min(values_set))
    while len(new_dict) > 3:
    # if len(new_dict) > 3: 
        # print(len(new_dict))
        # print(max(new_dict.values()))
        # print (new_dict)
        new_dict.pop([key for key, value in new_dict.items() if value == max(new_dict.values())][0])
    return new_dict

def main():
    new_point = [5,3,9]
    file = "coordinate_data.csv"
    output_dict = dict(csvReader(file))
    distance_dict = distance(output_dict, new_point)
    print(distance_dict)
    display(output_dict)


    #Notes to self
    #Get specified amount of max values
    #Link all values to their alphabet variable
    #Add the check to add 0 if an array is missing a value

if __name__ == '__main__':
    main()


# for the baby's name see what things have the most that match and then use the values of that
# to see what is closest