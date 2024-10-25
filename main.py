def binary_to_decimal(binary_str):
    decimal = int(binary_str, 2)
    return decimal

binary_str = input("Enter your Binary: ")

decimal_number = binary_to_decimal(binary_str)

print("Decimal:", decimal_number)
