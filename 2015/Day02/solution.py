def find_box_surface_area(dim):
    l, w, h = int(dim[0]), int(dim[1]), int(dim[2])
    return 2 * l * w + 2 * w * h + 2 * h * l


def find_smallest_sides(dim):
    dim_list = [int(dim[0]), int(dim[1]), int(dim[2])]
    dim_list.sort()
    return [dim_list[0], dim_list[1]]


def find_box_smallest_area(dim):
    edge1, edge2 = find_smallest_sides(dim)
    return edge1 * edge2


def find_box_ribbon(dim):
    edge1, edge2 = find_smallest_sides(dim)
    return (edge1 + edge2)*2


def find_box_ribbon_for_bow(dim):
    l, w, h = int(dim[0]), int(dim[1]), int(dim[2])
    return l * w * h


file = open("input.txt")
wrapping_paper_needed = 0
ribbon_needed = 0
for line in file:
    dim = line.split('x')
    wrapping_paper_needed += find_box_surface_area(dim) + find_box_smallest_area(dim)
    ribbon_needed += find_box_ribbon(dim) + find_box_ribbon_for_bow(dim)

print("they should order", wrapping_paper_needed, "square feet of wrapping paper")
print("they should order", ribbon_needed, "feet of ribbon")
