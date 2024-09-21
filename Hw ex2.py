good_jumps_count = 0
good_jumps_sum = 0
highest_jump = 0
world_record = 6.23
record_breaker = None

for i in range(7):
    jump = float(input("Enter jump result in meters: "))

    if jump < 5.80:
        continue

    good_jumps_count += 1
    good_jumps_sum += jump
    if jump > highest_jump:
        highest_jump = jump

    if jump > world_record:
        world_record = jump
        record_breaker = input("Enter the name of the athlete who broke the record: ")

if good_jumps_count > 0:
    average_jump = good_jumps_sum / good_jumps_count
    print(f"Number of good jumps: {good_jumps_count}")
    print(f"Average of good jumps: {average_jump}")
    print(f"Highest jump: {highest_jump}")
else:
    print("No good jumps recorded.")

if record_breaker:
    print(f"New world record: {world_record} meters by {record_breaker}")
else:
    print("No new world record.")
