import random

def quick_sort(low, high):

    if high > low:
        result_value = random_swap(low, high)
        quick_sort(low, result_value)
        quick_sort(result_value + 1, high)

def swap(low, high):

    global Value
    result = Value[low]
    low_value = low

    for high_value in range(low + 1, high + 1):
        if Value[high_value] < result:
            low_value += 1
            print(Value)
            Value[high_value], Value[low_value] = Value[low_value], Value[high_value]

    result_value = low_value
    Value[low], Value[result_value] = Value[result_value], Value[low]

    return result_value

def random_swap(low, high):

    global Value

    random_value = random.randrange(low, high + 1)
    Value[low], Value[random_value] = Value[random_value], Value[low]

    return swap(low, high)

number = int(input("크기 : "))
Value = []

for i in range(0, number):
    Value.append(int(input()))

quick_sort(0, number - 1)

for i in Value:
    print(i, end = ' ')