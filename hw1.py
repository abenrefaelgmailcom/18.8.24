positive_count = 0
negative_count = 0
zero_count = 0
divisible_by_7_count = 0
last_positive = None
last_negative = None

for i in range(10):
    number = int(input("Enter a number: "))

    if number == -9999:
        print("Exit loop.")
        break

    if number > 1000 or number < -1000:
        continue

    if number > 0:
        positive_count += 1
        last_positive = number
    elif number < 0:
        negative_count += 1
        last_negative = number
    else:
        zero_count += 1

    if number % 7 == 0:
        divisible_by_7_count += 1
else:
    print(f"Positive numbers count: {positive_count}")
    print(f"Negative numbers count: {negative_count}")
    print(f"Zero count: {zero_count}")
    print(f"Numbers divisible by 7: {divisible_by_7_count}")
    print(f"Last positive number: {last_positive}")
    print(f"Last negative number: {last_negative}")
