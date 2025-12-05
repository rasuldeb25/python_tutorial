# format specifiers = {:flags} format a value based on what flag is inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = coma seperator

price1 = 314121312.311241
price2 = -98.65
price3 = -12.34

print(f"Price 1 is: ${price1:,.2f}")
print(f"Price 2 is: ${price2:^10}")
print(f"Price 3 is: ${price3:^10,.1f}")