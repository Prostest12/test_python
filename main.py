import re

# 1 задание

s = 'Адрес 54\\45. Номер 40\\59  6622\\66333'
result = []


def good_number(string):
    pattern = r"(\d{2,4})\\(\d{2,5})"
    matches = re.findall(pattern, string)
    for match in matches:
        good_number = f"{int(match[0]):04d}\\{int(match[1]):05d}"
        result.append(good_number)
    return result


print(good_number(s))

# 2 задание

def add_atms(n, k, distances):

    result= list()

    for i in range(k) :
        max_num = max(distances)
        max_index = distances.index(max_num)
        last_pos = max(distances)

        distances[max_index] =  last_pos/2
        distances.insert(max_index, last_pos / 2)

    return distances

n = 5
k = 3
distances = [100, 180, 50, 60, 150]

new_distances = add_atms(n, k, distances)

print(new_distances)

# 3 задание

def max_concatenated_number(lst):
    sorted_lst = sorted(lst, reverse=True)
    concatenated_str = ''.join(sorted_lst)
    return int(concatenated_str)
lst = ['50', '2', '1', '9']
print(max_concatenated_number(lst))
