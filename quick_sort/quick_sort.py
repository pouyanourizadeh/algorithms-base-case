target_list = [5,4,3,2,1]

def helper_function(the_list, start_index, end_index):

    # set the las
    pivot = the_list[end_index]

    left_index = start_index
    right_index = end_index - 1

    # loop until left and right reach the pivot point
    while left_index <= right_index:
        
        # loop until finding an index that doesn't belong to left or right list
        while left_index <= end_index and the_list[left_index] < pivot:
            left_index += 1
        while right_index >= start_index and the_list[right_index] < pivot:
            right_index -= 1
        
        # swap if found a case
        if the_list[left_index] > the_list[right_index]:
            the_list[left_index], the_list[right_index] = the_list[right_index], the_list[left_index]

        # put pivot element back
        else:
            the_list[end_index], the_list[left_index] = the_list[left_index], the_list[end_index]

def quick_sort(the_list, start_index, end_index):

    if start_index >= end_index:
        return the_list

    pivot_point = helper_function(the_list, start_index, end_index)

    # splitting the array in two and recursively calling the function
    quick_sort(the_list, start_index, pivot_point - 1)
    quick_sort(the_list, pivot_point+1, end_index)


quick_sort(target_list, 0, len(target_list)-1)