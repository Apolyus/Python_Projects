def i_do_sums_for_args(*args, param_1=3):
    sum_of_elements = 0
    for each_element in args:
        if isinstance(each_element, int):
            sum_of_elements += each_element
    return sum_of_elements


print("First Sum : ", i_do_sums_for_args(1, 5, -3, "abc", [12, 56, "cad"] ))
print("Second Sum : ", i_do_sums_for_args())
print("Third Sum : ", i_do_sums_for_args(2, 4, "abc", param_1=2))


def i_do_sums_for_inputs(nums) -> int:
    sum1 = 0
    for numbers_from_input in range(nums):
        sum1 += numbers_from_input
    return sum1


input_numbers = int(input("Put number : "))
print(i_do_sums_for_inputs(input_numbers))


def i_dont_know_names(giraffe: int) -> int:
    if giraffe % 2 == 0:
        return giraffe
    else:
        return 0


el_inputadore = input("Put a number: ")
print(i_dont_know_names(int(el_inputadore)))