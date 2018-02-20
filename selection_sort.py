# input data
my_list = [5, 3, 6, 2, 10]


# find Maximum
# @list: the list for finding the maximum
# @return : the maximum_index in the list
def find_maximum(max_list):
    maximum = max_list[0]
    maximum_index = 0
    for i in range(1, len(max_list)):
        if maximum < max_list[i]:
            maximum = max_list[i]
            maximum_index = i

    return maximum_index


# selection_sort ---- Des
# @sort_list: the list for sorting
# @return : the list after sorting
def selection_sort(sort_list):
    result = []
    length = len(sort_list)
    for i in range(length):
        index = find_maximum(sort_list)
        result.append(sort_list[index])
        del sort_list[index]
    return result


# test section
print(selection_sort(my_list))
