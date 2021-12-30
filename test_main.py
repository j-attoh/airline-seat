from main import compute_passenger_seating, InputError
import pytest
from collections import namedtuple


def test_must_be_array():
    with pytest.raises(InputError) as excinfo:
        compute_passenger_seating("this is getting funny")
    assert "Must be A List" in str(excinfo.value)


def test_must_be_2D_in_array():
    with pytest.raises(InputError) as excinfo:
        compute_passenger_seating([[1, 2, 3], [4, 5, 6], [5, 6, 9]])

    assert "Must be a 2D array" in str(excinfo.value)


def test_type_of_array():
    with pytest.raises(InputError) as excinfo:
        compute_passenger_seating([[1, "joe"], ["ama", "akosua"]])

    assert "Must be 2D integer array" in str(excinfo.value)


def test_must_be_adequate_seating_capacity():
    with pytest.raises(InputError) as excinfo:
        seats = [[3, 2], [4, 3], [2, 3], [3, 4]]
        seat_sum = sum(x[0] * x[1] for x in seats)
        compute_passenger_seating(seats, intimated_num_of_passengers=1000)
    assert f'Seating Capacity of "{seat_sum}"' in str(excinfo.value)


def test_seating_arrangement():
    first_seat = [[3, 2], [4, 3], [2, 3], [3, 4]]
    other_seat = [[4, 3], [2, 4], [3, 2], [3, 4]]
    # seats = [(first_seat, 30), (other_seat, 38)]
    Seat = namedtuple("Seat", ["array", "num_of_passengers"])
    seats = [Seat(first_seat, 30), Seat(other_seat, 38)]
    expected_first_output = [
        [[19, 25, 1], [21, 29, 7]],
        [[2, 26, 27, 3], [8, 30, "", 9], [13, "", "", 14]],
        [[4, 5], [10, 11], [15, 16]],
        [[6, 28, 20], [12, "", 22], [17, "", 23], [18, "", 24]],
    ]

    expected_other_output = [
        [[20, 27, 28, 1], [22, 31, 32, 7], [24, 35, 36, 13]],
        [[2, 3], [8, 9], [14, 15], [17, 18]],
        [[4, 29, 5], [10, 33, 11]],
        [[6, 30, 21], [12, 34, 23], [16, 37, 25], [19, 38, 26]],
    ]
    expected_outputs = [expected_first_output, expected_other_output]
    for (index, seat) in enumerate(seats):
        output = compute_passenger_seating(seat.array, seat.num_of_passengers)
        assert expected_outputs[index] == output
