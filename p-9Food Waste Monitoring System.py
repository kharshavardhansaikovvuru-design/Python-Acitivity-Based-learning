# Food Waste Monitoring System

days = []
n = int(input("Enter the number of days: "))

waste_limit = float(input("Enter acceptable wastage percentage: "))

total_prepared = 0
total_served = 0
total_leftovers = 0

for i in range(n):
    print("\nEnter details for Day", i + 1)

    day = input("Enter day name: ")
    prepared = int(input("Enter number of meals prepared: "))
    served = int(input("Enter number of meals served: "))
    leftovers = int(input("Enter number of leftover meals: "))

    # Validate meal quantities
    if prepared < 0 or served < 0 or leftovers < 0:
        print("Invalid input! Quantities cannot be negative.")
        continue

    if served + leftovers > prepared:
        print("Invalid data! Served meals and leftovers exceed prepared meals.")
        continue

    # Calculate wastage percentage
    if prepared > 0:
        wastage_percentage = (leftovers / prepared) * 100
    else:
        wastage_percentage = 0

    # Store daily details
    days.append([
        day, prepared, served, leftovers, wastage_percentage
    ])

    total_prepared += prepared
    total_served += served
    total_leftovers += leftovers

# Display daily report
print("\n========== FOOD WASTE MONITORING REPORT ==========")
print("Day\tPrepared\tServed\tLeftovers\tWastage %")

for d in days:
    print(d[0], "\t", d[1], "\t\t", d[2], "\t",
          d[3], "\t\t", round(d[4], 2), "%")

    if d[4] > waste_limit:
        print("Warning: Wastage exceeds acceptable limit on", d[0])
    else:
        print("Wastage is within the acceptable limit on", d[0])

# Calculate overall wastage percentage
print("\n========== OVERALL SUMMARY ==========")
print("Total Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftover Meals:", total_leftovers)

if total_prepared > 0:
    overall_wastage = (total_leftovers / total_prepared) * 100
    print("Overall Wastage Percentage:",
          round(overall_wastage, 2), "%")
else:
    print("Overall Wastage Percentage: 0%")

print("==================================================")