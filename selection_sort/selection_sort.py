
def insertion_sort(the_list):

    for i in range(len(the_list)):
        smallest_index = i
        for j in range(i+1,len(the_list)):
            if the_list[j] < the_list[smallest_index]:
                smallest_index = j
        
        the_list[smallest_index], the_list[i] = the_list[i], the_list[smallest_index]
    print the_list

the_list = [1234,235,4567,678,23,45,6756,3]
print the_list
insertion_sort(the_list)