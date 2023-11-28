
def part_one():
    up = 0
    down = 0
    file = open("input.txt")
    for file_obj in file:
        for line in file_obj:
            for char in line:
                if char == '(':
                    up += 1
                elif char == ')':
                    down += 1

    floor = up - down
    print("Santa needs to take the intructions for this floor:", floor)


def part_two():
    up = 0
    down = 0
    file = open("input.txt")
    for file_obj in file:
        for line in file_obj:
            for char in line:
                if char == '(':
                    up += 1
                elif char == ')':
                    down += 1

                floor = up - down
                if floor == -1:
                    position = up+down
                    print("This position of the character that causes Santa to first enter the basement:", position)
                    return

part_one()
part_two()
