def quick_sort(input):
    if len(input) <=1:
        return input
    else :
        pivot=input.pop()
    small_pivot = []
    large_pivot = []
        
    for i in range(len(input)):
            if input[i] <= pivot:
                small_pivot.append(input[i])
            else:
                large_pivot.append(input[i])

    return quick_sort(small_pivot)+[pivot]+quick_sort(large_pivot)



# def quick_sort(sequence):
#     length = len(sequence)
#     if length <= 1:
#         return sequence
#     else:
#         pivot = sequence.pop()

#     items_greater = []
#     items_lower = []

#     for item in sequence:
#         if item > pivot:
#             items_greater.append(item)

#         else:
#             items_lower.append(item)

#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


lis=[1,3,2,8,7,4,6,20]
print(quick_sort(lis))
print(lis)