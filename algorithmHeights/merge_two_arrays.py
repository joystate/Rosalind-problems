import os
import string

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'sourse.txt'))
content = f.readlines()
string_array_1 = content[1].split()
string_array_2 = content[3].split()
sorted_array_1 = []
sorted_array_2 = []
for i in string_array_1:
    sorted_array_1.append(int(i))
for j in string_array_2:
    sorted_array_2.append(int(j))

def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    expected_length = len(arr1)+len(arr2)
    for k in range(0, expected_length):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            if i < len(arr1)-1:
                i += 1
            else:
                result += arr2[j:]
                break
        elif arr2[j] < arr1[i]:
            result.append(arr2[j])
            wasFromSecond = True
            if j < len(arr2)-1:
                j += 1
            else:
                result += arr1[i:]
                break
        else:
            result.append(arr2[j])
            result.append(arr1[i])
            if i < len(arr1)-1:
                i += 1
            else:
                result += arr2[j:]
                break
            if j < len(arr2)-1:
                j += 1
            else:
                result += arr1[i:]
                break
    string_result = []
    for i in result:
        string_result.append(str(i))
    return string.join(string_result)


if __name__ == "__main__":
    print merge(sorted_array_1, sorted_array_2)

