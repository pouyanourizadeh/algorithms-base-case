
def bubble_sort(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(n-1):
            if list_a[j] > list_a[
                j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                print list_a

list_a = [123,6,56756,3,46436,5645,342,6789,9,56,7,125]

bubble_sort(list_a)