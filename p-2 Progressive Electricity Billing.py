# Progressive Electricity Billing System

months = ["January", "February", "March", "April"]
bills = []

fixed_charge = 50
surcharge_rate = 5
rebate_rate = 2

for month in months:
    units = int(input("Enter electricity units consumed in " + month + ": "))

    # Calculate charges using progressive slabs
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Calculate surcharge and rebate
    surcharge = energy_charge * surcharge_rate / 100
    rebate = energy_charge * rebate_rate / 100

    # Calculate total bill
    total_bill = energy_charge + fixed_charge + surcharge - rebate

    bills.append(total_bill)

    print("\nMonth:", month)
    print("Units Consumed:", units)
    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Electricity Bill: Rs.", round(total_bill, 2))

# Compare bills across months
print("\n--- Monthly Bill Comparison ---")

for i in range(len(months)):
    print(months[i], ": Rs.", round(bills[i], 2))

# Identify unusual increases
for i in range(1, len(bills)):
    increase = bills[i] - bills[i - 1]

    if increase > 0:
        percentage = (increase / bills[i - 1]) * 100

        if percentage > 25:
            print("\nWarning: Unusual bill increase detected!")
            print("From", months[i - 1], "to", months[i])
            print("Increase: Rs.", round(increase, 2))
            print("Percentage Increase:", round(percentage, 2), "%")
        else:
            print("\nBill increase from", months[i - 1], "to", months[i],
                  "is", round(percentage, 2), "%")
    elif increase < 0:
        print("\nBill decreased from", months[i - 1], "to", months[i])
    else:
        print("\nBill remained unchanged from", months[i - 1], "to", months[i])