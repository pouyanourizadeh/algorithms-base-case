
def insertion_sort(the_list):

    # For each item in the input list
    for index in xrange(len(the_list)):

        # Shift it to the left until it's in the right spot
        while index > 0 and the_list[index - 1] >= the_list[index]:
            the_list[index], the_list[index - 1] =\
                the_list[index - 1], the_list[index]
            index -= 1
    print the_list


the_list = [123,234,235,456,465786,523,243,234,235,56,456,457,456,234]
print the_list
insertion_sort(the_list)