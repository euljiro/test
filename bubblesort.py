# input = [4, 6, 2, 9, 1]


# def bubble_sort(array):
#     for i in range(len(input)-1):
#         for j in range(len(input) - i -1):
#             if input[j] > input[j+1]:
#                 input[j], input[j+1] = input[j+1],input[j]
#     return


# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!



# input = [4, 6, 2, 9, 1]
# n= len(input)


# def selection_sort(array):
#     for i in range(n-1):
#         min_index=i 
#         for j in range(n-i):
#             if array[i+j] < array[min_index]:
#                 min_index = i+j
#             array[min_index], array[i] = array[i] , array[min_index]

#     return


# selection_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!




# input = [4, 6, 2, 9, 1]
# n= len(input)

# def selection_sort(array):
#     for i in range(1, n):
#         for j in range(i): #i가 늘어날 때마다 j에서 반복하는 횟수가 증가
#             if array[i-j-1] > array[i-j]:
#                 array[i - j- 1], array[i-j] = array[i-j] , array[i-j-1]
#             else:
#                 break

#     return


# selection_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!





array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array_c=[]
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1
    if array1_index == len(array1):
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
            array1_index += 1

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

