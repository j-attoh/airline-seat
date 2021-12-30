from typing import List


class Error(Exception):
    """Base class of exceptions in this module."""

    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which error occured
        message -- explanation of the error

    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def compute_passenger_seating(
    seating_array=[[3, 2], [4, 3], [2, 3], [3, 4]], intimated_num_of_passengers=30
):
    """
    Computing airline seating arrangement in line with specified rules

    checking errors
        if intimated_num_of_passengers greater than capacity
        if elements are not 2D arrays
        if elements are not integers

    """

    """
    seats = []
    for item in seating_array:
        output = []
        for row in range(item[1]):
            output.append(["X" for _ in range(item[0])])
        seats.append(output)

    """
    if not isinstance(seating_array, List):
        raise InputError(seating_array, "Must be A List")
    for item in seating_array:
        if len(item) != 2:
            raise InputError(item, "Must be a 2D array")
        if not [int, int] == [type(x) for x in item]:
            raise InputError(item, "Must be 2D integer array")

    if sum(x[0] * x[1] for x in seating_array) < intimated_num_of_passengers:
        raise InputError(
            intimated_num_of_passengers,
            (
                f'Seating Capacity of "{sum(x[0] * x[1] for x in seating_array )}" '
                f'Insufficient less than "{intimated_num_of_passengers}"',
            ),
        )

    NUM_OF_SEATING_GROUPS = len(seating_array)  # count of number of 2D arrays
    cols = [x[0] for x in seating_array]
    rows = [x[1] for x in seating_array]

    easy_seating = []

    while sum(rows) != 0:
        for (index, value) in enumerate(cols):
            r = ["" for x in range(value)] if rows[index] != 0 else []
            if r:
                print(r)
            easy_seating.append(r)
            if rows[index] > 0:
                rows[index] -= 1

    num = 1

    # aisle seating arrangement
    for (index, value) in enumerate(easy_seating):
        if num < intimated_num_of_passengers:
            if value and (index + 1) % NUM_OF_SEATING_GROUPS == 1:
                value[-1] = num
                num += 1
                easy_seating[index] = value
            elif value and (index + 1) % NUM_OF_SEATING_GROUPS not in [0, 1]:
                value[0] = num
                num += 1
                value[-1] = num
                num += 1
                easy_seating[index] = value
            elif value and (index + 1) % NUM_OF_SEATING_GROUPS == 0:
                value[0] = num
                num += 1
                easy_seating[index] = value
        else:
            break

    # window seating arrangement
    for (index, value) in enumerate(easy_seating):
        if num < intimated_num_of_passengers:
            if value and (index + 1) % NUM_OF_SEATING_GROUPS == 1:
                value[0] = num
                num += 1
                easy_seating[index] = value
            elif value and (index + 1) % NUM_OF_SEATING_GROUPS == 0:
                value[-1] = num
                num += 1
                easy_seating[index] = value
        else:
            break

    # center seating arrangement
    for (index, value) in enumerate(easy_seating):
        if value and len(value) > 2:
            for i in range(1, len(value[1:-1]) + 1):
                if num > intimated_num_of_passengers:
                    break
                value[i] = num
                num += 1
        easy_seating[index] = value

    print()

    """
    for seat in easy_seating:
        print(seat)
    """

    output = [[] for _ in range(NUM_OF_SEATING_GROUPS)]
    for (index, seat) in enumerate(easy_seating):
        if seat:
            output[((index + 1) % 4) - 1].append(seat)
    import pprint

    pp = pprint.PrettyPrinter(indent=4, compact=True)
    pp.pprint(output)
    return output


if __name__ == "__main__":
    compute_passenger_seating()
