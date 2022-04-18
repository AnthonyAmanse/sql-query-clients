from dateutil import parser

def range_to_timefilter(iso_date_from, iso_date_to):
    from_parsed = parser.parse(iso_date_from)
    to_parsed = parser.parse(iso_date_to)
    from_day = from_parsed.day
    from_month = from_parsed.month
    from_year = from_parsed.year
    to_day = to_parsed.day
    to_month = to_parsed.month
    to_year = to_parsed.year

    ## year has difference
    if (to_year - from_year > 0):
        additional_or = ""
        # if months are still remaining in from range of year
        if (from_month < 12):
            additional_or += "OR (YEAR = {0} AND MONTH > {1}) ".format(from_year, from_month)
        # if there are years in between from and to
        if (to_year - from_year > 2):
            additional_or += "OR (YEAR BETWEEN {0} AND {1}) ".format(from_year + 1, to_year - 1)
        elif (to_year - from_year == 2):
            additional_or += "OR (YEAR = {0}) ".format(from_year + 1)
        # if months are still remaining in to range of year
        if (to_month > 1):
            additional_or += "OR (YEAR = {0} AND MONTH < {1}) ".format(to_year, to_month)

        return "(YEAR = {0} AND MONTH = {1} AND DAY >= {2}) {6}OR (YEAR = {3} AND MONTH = {4} AND DAY <= {5})"\
            .format(from_year, from_month, from_day, to_year, to_month, to_day, additional_or)

    ## month has difference
    if (to_month - from_month > 0):
        additional_or = ""
        difference = to_month - from_month
        if (difference > 2):
            additional_or = "OR (YEAR = {0} AND MONTH BETWEEN {1} AND {2}) ".format(from_year, from_month + 1, to_month - 1)
        elif (difference == 2):
            additional_or = "OR (YEAR = {0} AND MONTH = {1}) ".format(from_year, from_month + 1)

        return "(YEAR = {0} AND MONTH = {1} AND DAY >= {2}) {5}OR (YEAR = {0} AND MONTH = {3} AND DAY <= {4})"\
                .format(to_year, from_month, from_day, to_month, to_day, additional_or)

    ## compare day if years and months are the same
    day_operator = ""
    days_difference = to_day - from_day
    if (days_difference == 0):
        day_operator = "= {0}".format(to_day)
    elif (days_difference == 1):
        day_operator = "IN ({0},{1})".format(from_day, to_day)
    elif (days_difference > 1):
        day_operator = "BETWEEN {0} AND {1}".format(from_day, to_day)

    return "YEAR = {0} AND MONTH = {1} AND DAY {2}".format(to_year, to_month, day_operator)