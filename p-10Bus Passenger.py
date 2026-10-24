# Bus Passenger Occupancy Simulation

passengers = int(input("Enter initial number of passengers: "))
capacity = int(input("Enter maximum bus capacity: "))
n = int(input("Enter number of stops: "))

if passengers < 0 or capacity <= 0 or passengers > capacity or n <= 0:
    print("Invalid initial input!")
else:
    total_boarded = 0
    total_alighted = 0
    violations = 0

    print("\n========== BUS OCCUPANCY REPORT ==========")

    for i in range(n):
        print("\nStop", i + 1)

        boarded = int(input("Enter number of passengers boarding: "))
        alighted = int(input("Enter number of passengers alighting: "))

        # Validate passenger counts
        if boarded < 0 or alighted < 0:
            print("Invalid passenger count! Enter non-negative values.")
            continue

        if alighted > passengers:
            print("Invalid transaction! More passengers cannot alight than are on the bus.")
            continue

        # Update passenger count
        passengers = passengers - alighted + boarded

        total_boarded += boarded
        total_alighted += alighted

        print("Passengers after stop:", passengers)

        # Check capacity
        if passengers > capacity:
            print("WARNING: Bus capacity exceeded!")
            violations += 1
        else:
            print("Bus occupancy is within capacity.")

    # Final summary
    print("\n========== FINAL SUMMARY ==========")
    print("Total Passengers Boarded:", total_boarded)
    print("Total Passengers Alighted:", total_alighted)
    print("Final Passenger Count:", passengers)
    print("Maximum Bus Capacity:", capacity)
    print("Capacity Violations:", violations)

    if violations > 0:
        print("Result: Capacity violations detected.")
    else:
        print("Result: No capacity violations detected.")

    print("===================================")