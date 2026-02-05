trip_durations = [1.1,0.8,2.5,2.6]
trip_fare = (6.25,5.25,10.50,8.05)

trip = dict(zip(trip_durations, trip_fare))
print(trip)

trip_num = input("What trip do you want? (1-4): ")
trip_index = int(trip_num) - 1
print(f"Duration: {list(trip.keys())[trip_index]} miles")
print(f"Fare: ${list(trip.values())[trip_index]: 2f}")

trip_list = [
    {"duration": 1.1, "fare": 6.25},
    {"duration": 0.8, "fare": 5.25},
    {"duration": 2.5, "fare": 10.50},
    {"duration": 2.6, "fare": 8.05}
]