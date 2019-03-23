def find_next_flight(flight_list, start_point):
    for flight in flight_list:
        if flight[0] is start_point:
            return flight


def getItinerary(flight_list, start_point):
    flight_list_len = len(flight_list)
    result = [start_point]
    current_flight = (start_point, )
    while True:
        current_flight = find_next_flight(flight_list, current_flight[0])
        if current_flight is None:
            break
        flight_list.remove(current_flight)
        result.append(current_flight[1])
        current_flight = (current_flight[1],)
    if len(result) == flight_list_len+1:
        return result
    return None


# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
print(getItinerary([('SFO', 'HKO'), ('YYZ', 'SFO'),
                    ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
# NONE
print(getItinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
# ['A', 'B', 'C', 'A', 'C']
print(getItinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))
# NONE
print(getItinerary([('SFO', 'COM')], 'COM'))
