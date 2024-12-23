def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The final price after discount or the original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    while True:
        try:
            # Prompt user for input
            original_price = float(input("Enter the original price of the item: "))
            discount_percentage = float(input("Enter the discount percentage: "))

            # Ensure non-negative values
            if original_price < 0 or discount_percentage < 0:
                print("Prices and percentages cannot be negative. Please try again.")
                continue

            # Calculate the final price
            final_price = calculate_discount(original_price, discount_percentage)

            # Display the result
            if final_price < original_price:
                print(f"The final price after applying the discount is: ${final_price:.2f}")
            else:
                print(f"No discount applied. The original price is: ${original_price:.2f}")

            break  # Exit the loop if everything is valid
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
