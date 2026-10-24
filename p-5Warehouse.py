# Warehouse Inventory Reconciliation

products = []
n = int(input("Enter the number of products: "))

for i in range(n):
    print("\nEnter details for Product", i + 1)

    name = input("Enter product name: ")
    opening_stock = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing_stock = int(input("Enter actual closing stock: "))
    minimum_stock = int(input("Enter minimum stock required: "))

    # Calculate expected closing stock
    expected_stock = opening_stock + incoming - dispatched

    # Detect stock discrepancy
    discrepancy = closing_stock - expected_stock

    # Calculate replenishment requirement
    if closing_stock < minimum_stock:
        replenishment = minimum_stock - closing_stock
    else:
        replenishment = 0

    products.append([
        name, opening_stock, incoming, dispatched,
        expected_stock, closing_stock, discrepancy, replenishment
    ])

# Display inventory reconciliation report
print("\n========== INVENTORY RECONCILIATION REPORT ==========")
print("Product\tOpening\tIncoming\tDispatched\tExpected\tActual\tDifference\tReplenish")

for p in products:
    print(p[0], "\t", p[1], "\t", p[2], "\t\t",
          p[3], "\t\t", p[4], "\t", p[5], "\t",
          p[6], "\t\t", p[7])

    if p[6] > 0:
        print("Status: Excess stock detected for", p[0])
    elif p[6] < 0:
        print("Status: Stock shortage detected for", p[0])
    else:
        print("Status: Stock matched for", p[0])

    if p[7] > 0:
        print("Replenishment required:", p[7], "units")
    else:
        print("No replenishment required.")

print("\n========== REPORT COMPLETED ==========")
