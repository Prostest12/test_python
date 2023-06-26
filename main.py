import re

s = ' asdad fsafsa fsafasАдрес 54\\45. Номер 40\\59 fasfasfsaf fas 6622\\66333 a'
result = []


def good_number(string):
    pattern = r"(\d{2,4})\\(\d{2,5})"
    matches = re.findall(pattern, string)
    for match in matches:
        good_number = f"{int(match[0]):04d}\\{int(match[1]):05d}"
        result.append(good_number)
    return result


print(good_number(s))

