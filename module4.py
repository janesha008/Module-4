count = 0
with open("story.txt", "r") as file:
    for line in file:
        if not line.startswith('T'):
            count += 1

print("Number of lines not starting with 'T':", count)
