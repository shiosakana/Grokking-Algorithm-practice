# input data
my_list = [1, 2, 3, 4, 5, 6, 7]


# binary_search function
# @search_list : the list that we want to search
# @item : the target that we want to find in the search_list
# @return : if find the item
#              return the index of the item
#           else
#              return none
def binary_search(search_list, item):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = search_list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid

    return None


# test section
print(binary_search(my_list, 3))  # 3 in the my_list
print(binary_search(my_list,999))  # 999 not in the my_list
