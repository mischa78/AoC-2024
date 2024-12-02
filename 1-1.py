with open('input/1-1-left.txt', 'r') as file:
    left_sorted = sorted(
        int(line.strip()) 
        for line in file 
        if line.strip().isdigit()
    )

with open('input/1-1-right.txt', 'r') as file:
    right_sorted = sorted(
        int(line.strip()) 
        for line in file 
        if line.strip().isdigit()
    )

total = 0
for left_val, right_val in zip(left_sorted, right_sorted):
    total += abs(left_val - right_val)

print(f'Total: {total}')