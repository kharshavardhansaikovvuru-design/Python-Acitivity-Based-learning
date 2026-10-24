# Retail Billing with Multiple Discount Rules

products = []
total_amount = 0
total_tax = 0
total_discount = 0

n = int(input("Enter the number of products: "))

for i in range(n):
    print("\nEnter details for Product", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/electronics/clothing): ")
    price = float(input("Enter price per unit: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    # Category-specific tax rates
    if category == "food":
        tax_rate = 5
    elif category == "electronics":
        tax_rate = 18
    elif category == "clothing":
        tax_rate = 12
    else:
        tax_rate = 10

    tax = amount * tax_rate / 100

    # Threshold-based discount
    if amount >= 5000:
        discount_rate = 15
    elif amount >= 2000:
        discount_rate = 10
    elif amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = amount * discount_rate / 100

    # Maximum concession limit
    if discount > 1000:
        discount = 1000

    # Calculate item total
    item_total = amount + tax - discount

    products.append([name, category, price, quantity, amount,
                     tax_rate, tax, discount, item_total])

    total_amount += amount
    total_tax += tax
    total_discount += discount

# Generate itemized invoice
print("\n========== RETAIL INVOICE ==========")
print("Product\tCategory\tQty\tPrice\tAmount\tTax\tDiscount\tTotal")

for p in products:
    print(p[0], "\t", p[1], "\t", p[3], "\t",
          round(p[2], 2), "\t", round(p[4], 2), "\t",
          round(p[6], 2), "\t", round(p[7], 2), "\t",
          round(p[8], 2))

grand_total = total_amount + total_tax - total_discount

print("\nSubtotal: Rs.", round(total_amount, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Total Discount: Rs.", round(total_discount, 2))
print("Grand Total: Rs.", round(grand_total, 2))
print("====================================")