arr = list(input('input: '))

new_arr = []

for x in arr:
    if int(x) >= 1:
        new_arr.append(int(x))

min = min(new_arr)
max = max(new_arr)

expected_sum = 0

for i in range (min, max + 1):
    expected_sum += i
    
actual_sum = sum(new_arr)

missing_number = expected_sum - actual_sum

if missing_number == 0:
    missing_number = new_arr[-1] + 1

print(missing_number)

# Functionality: 3.5
# Performance: 3.5
# Quality: 3