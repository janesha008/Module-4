#EX 1
import math

class cse:
    def mech(self, r):
        area = math.pi * r * r
        print("Area of the circle:", area)

radius = float(input("Enter the radius of the circle: "))
obj = cse()
obj.mech(radius)

#EX 2
def merge(dict1, dict2):
    merged = {**dict1, **dict2}
    return merged

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'b': 10}

result = merge(dict1, dict2)
print("Merged dictionary:", result)

#EX 3
data = {'banana': 'yellow', 'apple': 'red', 'cherry': 'pink', 'grape': 'purple'}
sorted_by_keys = dict(sorted(data.items()))
sorted_by_values = dict(sorted(data.items(), key=lambda item: item[1]))
print("Original dictionary:", data)
print("Sorted by keys:", sorted_by_keys)
print("Sorted by values:", sorted_by_values)

#EX 4
list1 = [10, 20, 30, 40]

try:
    print(list1[5])
except IndexError:
    print("You're out of list range")

#EX 5
count = 0
with open("story.txt", "r") as file:
    for line in file:
        if not line.startswith('T'):
            count += 1

print("Number of lines not starting with 'T':", count)