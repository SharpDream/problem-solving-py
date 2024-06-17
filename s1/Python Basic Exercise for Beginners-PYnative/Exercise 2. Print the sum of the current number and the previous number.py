previous_num = 0

print("Printing current and previous number sum in a range(10)")

for current_num in range(10):
    print(f"Current Number {current_num} "
          f"Previous Number: {previous_num} "
          f"Sum: {current_num + previous_num}")

    previous_num = current_num
