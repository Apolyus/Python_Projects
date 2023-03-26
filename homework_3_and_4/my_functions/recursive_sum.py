def i_do_sums_for_inputs(nums: int) -> tuple:
    if nums == 0:
        return 0, 0, 0

    sum_total, sum_even, sum_odd = i_do_sums_for_inputs(nums-1)
    sum_total += nums
    if nums % 2 == 0:
        sum_even += nums
    elif nums % 2 != 0:
        sum_odd += nums

    return sum_total, sum_even, sum_odd
