file = open("input.txt")
up = 0
down = 0

for file_obj in file:
    for line in file_obj:
        for char in line:
            if char == '(':
                up += 1
            elif char == ')':
                down += 1

floor = up - down
print("floor: ", floor)
