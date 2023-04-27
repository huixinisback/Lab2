import numbers


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print (num_list)
    print (calc_average(num_list))
    find_min_max(num_list)
    return

def display_main_menu():
    print("display_main_menu")
    print("Enter some number seperated by a commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input().split(",")
    y = []
    for i in numbers :
        y.append(float(i))
    return y

def calc_average(numbers):
    print("calc_average")
    y = sum(numbers)/len(numbers)
    return y

def find_min_max(numbers):
    print("find_min_max")
    print("Max = " + str(max(numbers)))
    print("Min = "+ str(min(numbers)))


main()