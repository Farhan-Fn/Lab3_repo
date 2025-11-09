from lab2.lab2 import calc_average_temperature, calc_min_max_temperature, calc_median_temperature, sort_temperature

def test_calc_average_temperature():
    numbers = [10, 20, 30, 40, 50]
    expected_average = 30.0
    assert calc_average_temperature(numbers) == expected_average

    numbers = [5, 5, 5, 5]
    expected_average = 5.0
    assert calc_average_temperature(numbers) == expected_average

def test_calc_min_max_temperature():
    numbers = [10, 20, 5, 40, 15]
    expected_min_max = [5, 40]
    assert calc_min_max_temperature(numbers) == expected_min_max

    numbers = [100]
    expected_min_max = [100, 100]
    assert calc_min_max_temperature(numbers) == expected_min_max

def test_calc_median_temperature():
    numbers = [7, 3, 5]
    sorted_numbers = sort_temperature(numbers.copy())
    expected_median = 5
    assert calc_median_temperature(sorted_numbers) == expected_median

    numbers = [10, 20, 30, 40]
    sorted_numbers = sort_temperature(numbers.copy())
    expected_median = (20 + 30) / 2
    assert calc_median_temperature(sorted_numbers) == expected_median

    numbers = [42]
    sorted_numbers = sort_temperature(numbers.copy())
    expected_median = 42
    assert calc_median_temperature(sorted_numbers) == expected_median
