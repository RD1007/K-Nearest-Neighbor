import matplotlib.pyplot as plt
# from sklearn.neighbors import KNeighborsClassifier
import csv
from collections import defaultdict

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]


# plt.scatter(x, y, c=classes)
# plt.show()

# new_x = 8
# new_y = 21
# new_point = [(new_x, new_y)]

# data = list(zip(x, y))
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(data, classes)

# prediction = knn.predict(new_point)

# plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
# plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
# plt.show()
output_dict = dict()
columns = defaultdict(list)
with open("coordinate_data.csv") as fin:
    dr = csv.DictReader(fin)
    for row in dr:
        output_dict[row.get('letter')] = [float(row.get('x')), float(row.get('y')), float(row.get('z'))], row.get('color')
    # print(output_dict)

for keys, values in output_dict.items():
    plt.scatter(values[0][0], values[0][1], values[0][2], values[1])
    plt.text(x=values[0][0]-0.5, y=values[0][1]-0.5, s=f"{keys}")
plt.title("3D Plane")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()