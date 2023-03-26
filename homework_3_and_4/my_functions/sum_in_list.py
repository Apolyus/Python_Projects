def i_do_sums_for_args(*args, param_1=3, **kwargs):
    sum_of_elements = 0
    # For each element in args take the int and float values from the tuple and add them to a sum.
    # For each element in args that is a set , list or tuple call the function to do the sum of the unpacked arguments.
    # Same for kwargs.
    for each_element_arg in args:
        if isinstance(each_element_arg, (int, float)):
            sum_of_elements += each_element_arg
        elif isinstance(each_element_arg, (list, set, tuple)):
            sum_of_elements += i_do_sums_for_args(*each_element_arg)
    for each_element_kwarg in kwargs:
        if isinstance(each_element_kwarg, (int, float)):
            sum_of_elements += each_element_kwarg
        elif isinstance(each_element_kwarg, (list, set, tuple)):
            sum_of_elements += i_do_sums_for_args(*each_element_kwarg)
    return sum_of_elements
