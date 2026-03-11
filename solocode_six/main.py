from vehicle import Vehicle


def main():
    car = Vehicle("Generic SUV", 11, 2.9, 53)
    bus = Vehicle("Generic Schoolbus", 175, 7, 11.5)
    plane = Vehicle("Boeing 747", 48445, 6.5, 0.13)
    motorcycle = Vehicle("Efficient Motorcyle", 1.6, 3.5, 93)

    vehicles = [car, bus, plane, motorcycle]
    vehicles.sort(key=lambda x: x.cost_per_mile)
    print("Name: Range, CPM")
    for vehicle in vehicles:
        print(
            f"{vehicle._name:<20}: {vehicle.range:<7} mi, ${vehicle.cost_per_mile:.2f} per mile"
        )


if __name__ == "__main__":
    main()
