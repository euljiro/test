n=int(input())
n_list= list(map(int, input().split()))
n_list.sort()

m=int(input())
m_list=list(map(int, input().split()))
m_list.sort()

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    for i in range(len(m_list)):
        if array[current_guess] == target[i]:
            return 1
        elif array[current_guess] < target[i]:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return 0


result = is_existing_target_number_binary(m_list, n_list)
print(result)