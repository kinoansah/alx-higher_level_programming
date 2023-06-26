#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Get the elements from my_list_1 and my_list_2
            dividend = my_list_1[i]
            divisor = my_list_2[i]

            # Perform the division
            result = dividend / divisor

        except ZeroDivisionError:
            print("division by 0")
            result = 0

        except IndexError:
            print("out of range")
            result = 0

        except TypeError:
            print("wrong type")
            result = 0

        finally:
            # Append the division result to the result_list
            result_list.append(result)

        return result_list
