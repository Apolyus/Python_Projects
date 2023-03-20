from My_func.sum_in_list import i_do_sums_for_args
from My_func.recursive_sum import i_do_sums_for_inputs
from My_func.read_integer import i_read_function

if __name__ == '__main__':

    print("First Sum : ", i_do_sums_for_args(1, 5, -3, "abc", [12, 56, [43, 5.365, {465, 3445}, (3, 5, 5)], "cad"]))
    print("Second Sum : ", i_do_sums_for_args())
    print("Third Sum : ", i_do_sums_for_args(2, 4, "abc", param_1=2))

    x = int(input("Put the number : "))
    total_sum, even_sum, odd_sum = i_do_sums_for_inputs(x)
    print("total sum is : ", total_sum)
    print("even sum is : ", even_sum)
    print("odd sum is : ", odd_sum)

    x = i_read_function()
    print(x)
