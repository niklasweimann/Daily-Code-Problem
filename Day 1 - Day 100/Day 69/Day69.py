from functools import reduce


def get_largest_product(data: list):
    if len(data) < 3:
        raise Exception("List is too small!")

    data.sort()

    possible_max_products = [
        data[0]*data[1]*data[len(data)-1], data[len(data)-1] * data[len(data)-2]*data[len(data)-3]]

    if possible_max_products[0] > possible_max_products[1]:
        return (data[0], data[1], data[len(data) - 1])
    else:
        return (data[len(data)-1], data[len(data)-2], data[len(data)-3])


list = [-10, -10, 5, 2]
result = get_largest_product(list)
print("{} = {}".format(result, reduce(lambda x, y: x*y, result)))
