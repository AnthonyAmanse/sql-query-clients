from opsscale_filter import range_to_timefilter

# Tests for same year, month, day
def test_filter_same_day():
    output = range_to_timefilter("2022-02-10T00:00:00.000Z", "2022-02-10T23:59:59.000Z")
    expected = "YEAR = 2022 AND MONTH = 2 AND DAY = 10"
    assert output == expected

def test_filter_same_day_2():
    output = range_to_timefilter("2022-02-11T00:34:00.000Z", "2022-02-11T11:00:05.000Z")
    expected = "YEAR = 2022 AND MONTH = 2 AND DAY = 11"
    assert output == expected

# Tests for difference in day (same year and month)
def test_filter_one_day_difference():
    output = range_to_timefilter("2022-02-22T23:00:00.000Z", "2022-02-23T00:00:00.000Z")
    expected = "YEAR = 2022 AND MONTH = 2 AND DAY IN (22,23)"
    assert output == expected

def test_filter_two_day_difference():
    output = range_to_timefilter("2022-02-10T23:00:00.000Z", "2022-02-12T00:00:00.000Z")
    expected = "YEAR = 2022 AND MONTH = 2 AND DAY BETWEEN 10 AND 12"
    assert output == expected

# Tests for difference in month (same year)
def test_filter_one_month_difference():
    output = range_to_timefilter("2022-02-22T23:00:00.000Z", "2022-03-10T00:00:00.000Z")
    expected = "(YEAR = 2022 AND MONTH = 2 AND DAY >= 22) OR (YEAR = 2022 AND MONTH = 3 AND DAY <= 10)"
    assert output == expected

def test_filter_two_month_difference():
    output = range_to_timefilter("2022-02-22T23:00:00.000Z", "2022-04-10T00:00:00.000Z")
    expected = "(YEAR = 2022 AND MONTH = 2 AND DAY >= 22) OR (YEAR = 2022 AND MONTH = 3) OR (YEAR = 2022 AND MONTH = 4 AND DAY <= 10)"
    assert output == expected

def test_filter_more_than_two_month_difference():
    output = range_to_timefilter("2022-02-05T23:00:00.000Z", "2022-06-28T00:00:00.000Z")
    expected = "(YEAR = 2022 AND MONTH = 2 AND DAY >= 5) OR (YEAR = 2022 AND MONTH BETWEEN 3 AND 5) OR (YEAR = 2022 AND MONTH = 6 AND DAY <= 28)"
    assert output == expected

# Tests for difference in years
def test_filter_one_year_difference():
    output = range_to_timefilter("2021-02-10T00:00:00.000Z", "2022-02-10T23:59:59.000Z")
    expected = "(YEAR = 2021 AND MONTH = 2 AND DAY >= 10) OR (YEAR = 2021 AND MONTH > 2) OR (YEAR = 2022 AND MONTH < 2) OR (YEAR = 2022 AND MONTH = 2 AND DAY <= 10)"
    assert output == expected

def test_filter_one_year_difference_2():
    output = range_to_timefilter("2021-02-10T00:00:00.000Z", "2022-01-15T23:59:59.000Z")
    expected = "(YEAR = 2021 AND MONTH = 2 AND DAY >= 10) OR (YEAR = 2021 AND MONTH > 2) OR (YEAR = 2022 AND MONTH = 1 AND DAY <= 15)"
    assert output == expected

def test_filter_one_year_difference_3():
    output = range_to_timefilter("2021-12-10T00:00:00.000Z", "2022-03-15T23:59:59.000Z")
    expected = "(YEAR = 2021 AND MONTH = 12 AND DAY >= 10) OR (YEAR = 2022 AND MONTH < 3) OR (YEAR = 2022 AND MONTH = 3 AND DAY <= 15)"
    assert output == expected

def test_filter_one_year_difference_4():
    output = range_to_timefilter("2021-12-10T00:00:00.000Z", "2022-01-15T23:59:59.000Z")
    expected = "(YEAR = 2021 AND MONTH = 12 AND DAY >= 10) OR (YEAR = 2022 AND MONTH = 1 AND DAY <= 15)"
    assert output == expected

def test_filter_two_year_difference():
    output = range_to_timefilter("2020-02-10T00:00:00.000Z", "2022-02-10T23:59:59.000Z")
    expected = "(YEAR = 2020 AND MONTH = 2 AND DAY >= 10) OR (YEAR = 2020 AND MONTH > 2) OR (YEAR = 2021) OR (YEAR = 2022 AND MONTH < 2) OR (YEAR = 2022 AND MONTH = 2 AND DAY <= 10)"
    assert output == expected

def test_filter_two_year_difference_2():
    output = range_to_timefilter("2020-02-10T00:00:00.000Z", "2022-01-15T23:59:59.000Z")
    expected = "(YEAR = 2020 AND MONTH = 2 AND DAY >= 10) OR (YEAR = 2020 AND MONTH > 2) OR (YEAR = 2021) OR (YEAR = 2022 AND MONTH = 1 AND DAY <= 15)"
    assert output == expected

def test_filter_two_year_difference_3():
    output = range_to_timefilter("2020-12-10T00:00:00.000Z", "2022-03-15T23:59:59.000Z")
    expected = "(YEAR = 2020 AND MONTH = 12 AND DAY >= 10) OR (YEAR = 2021) OR (YEAR = 2022 AND MONTH < 3) OR (YEAR = 2022 AND MONTH = 3 AND DAY <= 15)"
    assert output == expected

def test_filter_two_year_difference_4():
    output = range_to_timefilter("2020-12-10T00:00:00.000Z", "2022-01-15T23:59:59.000Z")
    expected = "(YEAR = 2020 AND MONTH = 12 AND DAY >= 10) OR (YEAR = 2021) OR (YEAR = 2022 AND MONTH = 1 AND DAY <= 15)"
    assert output == expected

def test_filter_more_than_two_year_difference():
    output = range_to_timefilter("2019-02-10T00:00:00.000Z", "2022-02-10T23:59:59.000Z")
    expected = "(YEAR = 2019 AND MONTH = 2 AND DAY >= 10) OR (YEAR = 2019 AND MONTH > 2) OR (YEAR BETWEEN 2020 AND 2021) OR (YEAR = 2022 AND MONTH < 2) OR (YEAR = 2022 AND MONTH = 2 AND DAY <= 10)"
    assert output == expected

def test_filter_more_than_two_year_difference_2():
    output = range_to_timefilter("2019-02-10T00:00:00.000Z", "2022-01-15T23:59:59.000Z")
    expected = "(YEAR = 2019 AND MONTH = 2 AND DAY >= 10) OR (YEAR = 2019 AND MONTH > 2) OR (YEAR BETWEEN 2020 AND 2021) OR (YEAR = 2022 AND MONTH = 1 AND DAY <= 15)"
    assert output == expected

def test_filter_more_than_two_year_difference_3():
    output = range_to_timefilter("2019-12-10T00:00:00.000Z", "2022-03-15T23:59:59.000Z")
    expected = "(YEAR = 2019 AND MONTH = 12 AND DAY >= 10) OR (YEAR BETWEEN 2020 AND 2021) OR (YEAR = 2022 AND MONTH < 3) OR (YEAR = 2022 AND MONTH = 3 AND DAY <= 15)"
    assert output == expected

def test_filter_more_than_two_year_difference_4():
    output = range_to_timefilter("2019-12-10T00:00:00.000Z", "2022-01-15T23:59:59.000Z")
    expected = "(YEAR = 2019 AND MONTH = 12 AND DAY >= 10) OR (YEAR BETWEEN 2020 AND 2021) OR (YEAR = 2022 AND MONTH = 1 AND DAY <= 15)"
    assert output == expected