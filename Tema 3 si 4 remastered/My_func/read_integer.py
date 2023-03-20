def i_read_function():
    i_input = input("Put number : ")
    try:
        i_input = int(i_input)
    except ValueError:
        return 0
    return i_input
